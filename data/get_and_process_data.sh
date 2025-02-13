cd data/

wget https://raw.githubusercontent.com/idiap/Factual-Reporting-and-Political-Bias-Web-Interactions/main/data/mbfc_raw.csv

conda activate news-sci-bot
python3 process_data.py
conda deactivate
