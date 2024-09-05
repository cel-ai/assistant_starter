"""
Framework: Cel.ai
License: MIT License

Hello World using https://openrouter.ai/
---------------------------------------------------------------------------------------------

This is a simple example of an AI Assistant implemented using the Cel.ai framework.
It serves as a basic demonstration of how to get started with Cel.ai 
for creating intelligent assistants using Openrouter.ai hosted models.

Visit https://openrouter.ai/ for more information on Openrouter.ai
You need a valid API key to use the Openrouter.ai models.
Add the API key to the .env file as OPENROUTER_API_KEY

This script is part of the Cel.ai example series and is intended for educational purposes.

Usage:
------
Configure the required environment variables in a .env file in the root directory of the project.
The required environment variables are:

- Create a .env file in the root directory of the project.
- OPENROUTER_API_KEY: The API key for Openrouter.ai. You can get this from the Openrouter.ai website.
- TELEGRAM_TOKEN: The Telegram bot token for the assistant. You can get this from the BotFather on Telegram.
- Intall requirements.txt


"""
# LOAD ENV VARIABLES
import datetime
import os
import sys
from loguru import logger as log
# Load .env variables
from dotenv import load_dotenv
load_dotenv()

# Configure the loguru logger
log.remove()
log.add(sys.stdout, format="<level>{level: <8}</level> | "
    "<cyan>{file}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

# Import Cel.ai modules
from cel.connectors.telegram import TelegramConnector
from cel.gateway.message_gateway import MessageGateway, StreamMode
from cel.message_enhancers.smart_message_enhancer_openai import SmartMessageEnhancerOpenAI
from cel.assistants.macaw.macaw_assistant import MacawAssistant
from cel.prompt.prompt_template import PromptTemplate
from cel.assistants.function_context import FunctionContext
from cel.assistants.function_response import RequestMode
from cel.assistants.common import Param
from cel.assistants.macaw.custom_chat_models.chat_open_router import \
    ChatOpenAIOpenRouter,\
    ChatOpenRouter
from cel.assistants.macaw.macaw_settings import MacawSettings


def current_date_and_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Setup prompt
prompt = """You are an AI assistant called {assistant_name}, you are here to help with 
crypto related questions. You can ask me anything about cryptocurrencies, 
blockchain, and related topics.
Today is {date}
Location: {location}
"""
    
prompt_template = PromptTemplate(prompt)

# Create the assistant based on the Macaw Assistant 
# NOTE: Make sure to provide api key in the environment variable `OPENROUTER_API_KEY`
# add this line to your .env file: OPENROUTER_API_KEY=your-key
# or uncomment the next line and replace `your-key` with your OpenAI API key
# os.environ["OPENROUTER_API_KEY"] = "your-key.."
ast = MacawAssistant(
    prompt=prompt_template,
    llm = ChatOpenAIOpenRouter,
    settings=MacawSettings(core_model="openai/gpt-4o"),
    state={
        "assistant_name": os.environ.get("ASSISTANT_NAME", "Celai"),
        # current date and time
        "date": current_date_and_time,
        "location": "San Francisco, CA"
    }
)


# Create the Message Gateway - This component is the core of the assistant
# It handles the communication between the assistant and the connectors
gateway = MessageGateway(
    assistant=ast,
    host="127.0.0.1", 
    port=5005
)


# For this example, we will use the Telegram connector
conn = TelegramConnector(
    token=os.environ.get("TELEGRAM_TOKEN"), 
    # Try to set the stream mode to SENTENCE
    stream_mode=StreamMode.FULL
)
# Register the connector with the gateway
gateway.register_connector(conn)

# Then start the gateway and begin processing messages
gateway.run(enable_ngrok=True)

