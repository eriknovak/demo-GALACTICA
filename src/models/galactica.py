# type packages
from enum import Enum

# model packages
from transformers import AutoTokenizer, OPTForCausalLM

# ====================================================================
# Helper functions
# ====================================================================


class ModelAction(str, Enum):
    """The possible actions for the model."""

    CITATION = "Find Citation"
    QUESTION = "Answer Question"


def prepare_prompt(prompt: str, action: ModelAction) -> str:
    """Prepare the prompt for the model."""
    if action == ModelAction.CITATION:
        return f"{prompt} [START_REF]"
    elif action == ModelAction.QUESTION:
        return f"Question: {prompt} \nAnswer:"
    else:
        return prompt


def prepare_output(output: str, action: ModelAction) -> str:
    """Prepare the output for the model."""
    if action == ModelAction.CITATION:
        return output.split("[END_REF]")[0] + "[END_REF]"
    else:
        return output


# ====================================================================
# Model definition
# ====================================================================


class GALACTICA:
    def __init__(
        self, model_name: str = "facebook/galactica-125m", use_gpu=False
    ) -> None:
        """Initialize the model."""
        self.use_gpu = use_gpu
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = OPTForCausalLM.from_pretrained(
            model_name, device_map="auto" if self.use_gpu else None
        )

    def generate_text(
        self, prompt: str, action: ModelAction, max_length: int = 40
    ) -> str:
        """Generate text from the prompt."""
        prepared_prompt = prepare_prompt(prompt, action)
        input_ids = self.tokenizer(prepared_prompt, return_tensors="pt").input_ids
        if self.use_gpu:
            input_ids = input_ids.cuda()
        output = self.model.generate(
            input_ids,
            max_new_tokens=max_length,
            do_sample=False,
            num_beams=5,
            top_p=1.0,
            top_k=50,
            temperature=1.0,
        )
        return prepare_output(self.tokenizer.decode(output[0]), action)
