<h1 align="center">SciNews Bot for BlueSky</h1>
<div align="center">
    <img src="logo.png" width=200 height=200>
</div>
<br>

A simple, AI-powered bot to report daily news about environment, technology, science and energy on BlueSky.

## Installation and usage

### Local

> _Required: [conda](https://anaconda.org/anaconda/conda)_


- Clone the repository

```bash
git clone https://github.com/AstraBert/SciNewsBot.git
cd SciNewsBot
```

- Build the conda environment:

```bash
conda env create -f environment.yml
```

- Run the bot:

```bash
# Linux/macOS
bash run_bot.sh
# Windows
.\run_bot.ps1
```

### Docker (recommended)

> _Required: [Docker](https://docs.docker.com/desktop/), [docker compose](https://docs.docker.com/compose/)_

Docker setup is extremely easy:

- Clone the repository

```bash
git clone https://github.com/AstraBert/SciNewsBot.git
cd SciNewsBot
```

- Rename the [`.env.example`](./.env.example) file to `.env` and add your [Mistral API Key](https://console.mistral.ai/api-keys/), and your [BlueSky](https://bsky.app/) username and password.

```bash
mv .env.example .env
# Make sure to modify the fields of the .env file. 
# For example:
# mistral_api_key = "abcdefghi123"
# bsky_username = "a-cool-username.bsky.social"
# bsky_password = "Averysafepassword"
```

- Launch the Docker application:

```bash
# The -d option detaches the services execution from your active terminal
docker compose up [-d]
```

## Contributing

Contributions are always welcome! Follow the contributions guidelines reported [here](CONTRIBUTING.md).

## Funding

If you found this project useful, please consider to [fund it](https://github.com/sponsors/AstraBert) and make it grow: let's support open-source together!😊

## License and rights of usage

The software is provided under MIT [license](./LICENSE).

### Full documentation will come soon!👷‍♀️

