import gradio as gr

def divide(x):
  return 2/int(x)
  
gr.Interface(divide, "textbox", "textbox").launch()
