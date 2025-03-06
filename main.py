import random

def random_response(message, history):
    print("Message:", message)
    print("History:", history)
    return random.choice(["Yes", "No"])

import gradio as gr

gr.ChatInterface(
    fn=random_response, 
    type="messages"
).launch()