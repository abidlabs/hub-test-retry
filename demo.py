import gradio as gr

def divide(x):
  return 2/str(x)
  
gr.Interface(divide, "textbox", "textbox").launch()
