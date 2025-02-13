# Activate the Conda environment
conda activate news-sci-bot

# Run the bot indefinitely
while ($true) {
    # Run the script
    python scripts/main.py

    # Sleep for 12 hours (43200 seconds)
    Start-Sleep -Seconds 43200
}

conda deactivate