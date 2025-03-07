
# Easy way to make a chatbot

A chatbot powered by LLM with Langchain and gradio




## Installation

Easy to install and setup. paste those commands in your terminal. this will clone the repo, build the enviroment and run the the chatbot in your local api. just replace and put your hugging face api key for HUGGINGFACEHUB_API_TOKEN. if you want to use openai or something else. you may need to export those api token as your enviroment variable.

```bash
git clone https://github.com/stsaikat/chatbot.git
cd chatbot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export HUGGINGFACEHUB_API_TOKEN="your hugging face api key"
python main.py
```