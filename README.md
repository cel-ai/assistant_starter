<!-- A centered logo of celia -->
<p align="center">
  <img src="https://raw.githubusercontent.com/cel-ai/celai/30b489b21090e3c3f00ffea66d0ae4ac812bd839/cel/assets/celia_logo.png" width="250" />
</p>

# Assistant Starter

Cel.ai is a powerful Python framework designed to accelerate the development of omnichannel virtual assistants. Whether you need to integrate with platforms like WhatsApp, Telegram, or VoIP services such as VAPI.com, Cel.ai provides the tools and flexibility to get your assistant up and running quickly.

This project is a starting point for a AI assistant that can be deployed to any platform. It includes a basic implementation of a virtual assistant that can be extended to include more complex features.


## Setup

Download the project and navigate to the root directory.

Creeate a `.env` file in the root directory and add the following environment variables:

```
OPENROUTER_API_KEY=...
TELEGRAM_TOKEN=...
NGROK_AUTHTOKEN=...
ASSISTANT_NAME=...
```

## Create Python .venv (Optional)

```bash
python3.11 -m venv .venv
```

```bash
source .venv/bin/activate

# install requirements
pip install -r requirements.txt
```


## Run

```bash
python main.py
```


