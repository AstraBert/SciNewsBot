from mistralai import Mistral
from findNews import NewsArticle, csv
from pydantic import BaseModel, Field
from newspaper import Article
import json
from atproto import Client, client_utils

s = open("/run/secrets/mistral_key")
content = s.read()
api_key = content.replace("\n","")
s.close()
s = open("/run/secrets/bsky_usr")
content = s.read()
username = content.replace("\n","")
s.close()
s = open("/run/secrets/bsky_psw")
content = s.read()
password = content.replace("\n","")
s.close()


class SourceEval(BaseModel):
    is_trustworthy: bool = Field(description="True if the source is deemed trustworthy, false if not")
    is_on_topic: bool = Field(description="True if the article topic matches with the required topic, False if not")

class CatchyHeading(BaseModel):
    catchy_heading: str = Field(description="A 100 characters max. catchy heading for a BlueSky post")



model = "mistral-small-latest"

client = Mistral(api_key=api_key)
bsky_client = Client()
bsky_client.login(login=username, password=password)

def get_reliability_metrics(article: NewsArticle):
    data = csv[csv["source"] == article.publisher_url.replace("https://","")]
    jsondata = data.to_dict()
    jsondata.update({"article_title": article.title})
    jsondata.update({"macro_topic_to_cover": article.topic})
    jsonstring = json.dumps(jsondata, indent=4)
    return jsonstring

def evaluate_source(jsonstring: str):
    chat_response = client.chat.parse(
        model=model,
        messages=[
            {
                "role": "system", 
                "content": "You are a news source evaluator: based on a JSON object containing the source reliability metrics, the article title and the topic it should cover, you should tell the user if the source is trustworthy (please reply with True if this is the case, False if it is not) and if the topic the article covers is contained in the macro-topic specified in the 'macro_topic_to_cover' entry of the JSON object (please reply with True if this is the case, False if it is not)."
            },
            {
                "role": "user", 
                "content": jsonstring
            },
        ],
        response_format=SourceEval,
        max_tokens=256,
        temperature=0
    )
    final_scheme = chat_response.choices[0].message.parsed
    return final_scheme.is_trustworthy, final_scheme.is_on_topic

def process_article_nlp(article: NewsArticle):
    article_tp = Article(article.url)
    article_tp.download()
    article_tp.parse()
    article_tp.nlp()
    summ = article_tp.summary
    return summ

def create_bsky_post(summary: str, article: NewsArticle):
    try:
        chat_response = client.chat.parse(
            model=model,
            messages=[
                {
                    "role": "system", 
                    "content": "You are a skilled journalist and social media strategist whose task is to, starting from the summary of a news article and from its title, create a catchy summary (max. 100 characters) to use inside a BlueSky post. The heading MUST follow the content of the article"
                },
                {
                    "role": "user", 
                    "content": f"This is the summary of the article: {summary}\n\nThis is the title of the article: {article.title}"
                },
            ],
            response_format=CatchyHeading,
            max_tokens=256,
            temperature=0
        )
        final_scheme = chat_response.choices[0].message.parsed
        heading = final_scheme.catchy_heading
        text = client_utils.TextBuilder().text(heading+"\n\n").link("Link to the article", article.url)
        post = bsky_client.send_post(text)
        bsky_client.like(post.uri, post.cid)
        return True
    except Exception as e:
        return False
    
    
