import os
os.makedirs("offload", exist_ok=True)

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re

# Model Name
model_name = "EleutherAI/gpt-neo-1.3B"

# Load Tokenizer and Model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
    offload_folder="./offload"
)

# CBT Prompt for context
CBT_PROMPT = (
    "أنت معالج نفسي عماني تستخدم العلاج المعرفي السلوكي. "
    "أجوبتك يجب أن تكون داعمة، مهذبة، وباللهجة العمانية إن أمكن. "
    "رجاءً لا تكرر كلمات، وكن مختصراً وفعّالاً."
)



# Utility to remove repeated phrases
def remove_repetition(text):
    return re.sub(r'(\b.+?\b)(?:\s+\1\b)+', r'\1', text)

def generate_response(user_input):
    # Prepare the prompt
    prompt = f"{CBT_PROMPT}المستخدم: {user_input}\nالمعالج:"
    
    # Tokenize and move to appropriate device
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    
    # Generate with controls
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        repetition_penalty=1.5  # Prevent loops
    )
    
    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response_text = response.split("المعالج:")[-1].strip()
    
    # Remove any repeated patterns
    cleaned_response = remove_repetition(response_text)
    
    return cleaned_response
