# import the necessary packages
import os
import gradio as gr

# import the model
from src.models.galactica import GALACTICA, ModelAction

# import the dotenv file
import src.utils.dotenv

# ===================================================================
# Initialize the model
# ===================================================================

model_name = os.environ.get("MODEL_NAME", "facebook/galactica-125m")
use_gpu = os.environ.get("USE_GPU", "false").lower() == "true"

# Initialize the model
model = GALACTICA(model_name, use_gpu=use_gpu)

# ===================================================================
# Interface definition
# ===================================================================

# Define the gradio interface. Find more information here:
# https://www.gradio.app/docs/

# Define the interface inputs
gr_inputs = [
    gr.Textbox(lines=3, placeholder="Insert prompt here...", label="Prompt"),
    gr.Radio(
        [ModelAction.CITATION, ModelAction.QUESTION, ModelAction.GENERATION],
        value=ModelAction.CITATION,
        label="Action",
    ),
    gr.Slider(minimum=20, maximum=512, value=100, label="Max Length"),
]

# Define the interface outputs
gr_outputs = gr.Textbox(lines=10, label="Output")

# Define the interface examples
gr_examples = [
    ["The paper that introduced Multi-Head Attention", ModelAction.CITATION, 40],
    ["How is the Pytagorean theorem defined?", ModelAction.QUESTION, 40],
    [
        "Why is a Transformer model better than an RNN model?",
        ModelAction.QUESTION,
        40,
    ],
]

# Define the interface
gr_iface = gr.Interface(
    fn=model.generate_text,
    inputs=gr_inputs,
    outputs=gr_outputs,
    examples=gr_examples,
    allow_flagging="never",
    title=f"GALACTICA Demo ({model_name})",
    description="This demo allows you to interact with the GALACTICA model.",
)

if __name__ == "__main__":

    # ===============================================================
    # Server configuration and launch
    # ===============================================================

    server_name = os.environ.get("SERVER_NAME")
    server_port = int(os.environ.get("SERVER_PORT"))
    server_share = os.environ.get("SERVER_SHARE").lower() == "true"

    auth_username = os.environ.get("AUTH_USERNAME", None)
    auth_password = os.environ.get("AUTH_PASSWORD", None)

    gr_iface.launch(
        server_name=server_name,
        server_port=server_port,
        auth=(auth_username, auth_password)
        if auth_username and auth_password
        else None,
        share=server_share,
    )
