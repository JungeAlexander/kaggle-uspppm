import gradio as gr


def greet(anchor, target):
    return len(anchor + target)


anchor_input = gr.inputs.Textbox(lines=1, placeholder="Anchor")
target_input = gr.inputs.Textbox(lines=1, placeholder="Target")

sim_output = gr.outputs.Textbox(type="number", label="Similarity")

iface = gr.Interface(fn=greet, inputs=[anchor_input, target_input], outputs=sim_output)

if __name__ == "__main__":
    app, local_url, share_url = iface.launch()
