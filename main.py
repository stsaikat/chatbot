import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

import warnings
warnings.filterwarnings('ignore')

import datetime

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm, 
    memory = memory,
    verbose=False
)


def generate_response(message, history):
    reponse = conversation.predict(input=message)
    return reponse

import gradio as gr

gr.ChatInterface(
    fn=generate_response, 
    type="messages"
).launch()