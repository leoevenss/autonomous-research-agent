from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

def load_llm():
    model_name = "microsoft/phi-2"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )

    return pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=300,
        temperature=0.2,
        do_sample=False,
        return_full_text=False,
        pad_token_id=tokenizer.eos_token_id
    )