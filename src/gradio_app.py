import gradio as gr


def greet(name):
    return f"Hello {name}!!"


inputs = gr.inputs.Textbox(lines=2, placeholder="Name Here...")

iface = gr.Interface(fn=greet, inputs=inputs, outputs="text")

if __name__ == "__main__":
    app, local_url, share_url = iface.launch()
