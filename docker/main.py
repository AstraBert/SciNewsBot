from findNews import get_news, filter_news, topics
from processArticles import get_reliability_metrics, evaluate_source, process_article_nlp, create_bsky_post
import time

def pipeline(topic: str):
    news, topi = get_news(topic)
    print("Got news!")
    article = filter_news(news, topi)
    print("Filtered news!")
    if article is None:
        return "Failed"
    else:
        metrics = get_reliability_metrics(article)
        print(metrics)
        is_reliable, is_on_topic = evaluate_source(metrics)
        print(is_reliable, is_on_topic)
        if is_reliable and is_on_topic:
            summary = process_article_nlp(article)
            print("Processed article NLP!")
            b = create_bsky_post(summary, article)
            print("BlueSky post sent!")
            if b:
                return "Success"
            else:
                return "Failed"
        else:
            return "Failed"

if __name__ == "__main__":
    for topic in topics:
        print(topic)
        success = pipeline(topic)
        print(success)
        time.sleep(10800)
    

