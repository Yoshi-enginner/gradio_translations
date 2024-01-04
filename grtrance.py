import gradio as gr                   
from transformers import pipeline     
#English To French
translations = pipeline("translation_en_to_fr")

#called translate
def tranform(test):
    results = translations(test)
    return results[0]['translation_text']

interface = gr.Interface(fn=tranform, inputs="text",outputs="text")

interface.launch()