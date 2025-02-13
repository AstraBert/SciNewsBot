conda activate news-sci-bot

# run the bot infinitely
while true
do
    # the bot takes 12h to run
    python3 scripts/main.py
    # sleep other 12h
    sleep 43200
done

conda deactivate