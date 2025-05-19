from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

app = Flask(__name__)
CORS(app)

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name)

def trim_incomplete_sentence(text):
    # Find the last proper sentence-ending punctuation
    match = re.search(r'([.!?])[^.!?]*$', text)
    if match:
        end_index = match.end(1)
        return text[:end_index]
    return text

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    # Tokenize input
    inputs = tokenizer(user_input, return_tensors="pt", padding=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Generate response
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=200,
        min_length=50,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        eos_token_id=tokenizer.eos_token_id,
    )

    # Decode and trim
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = trim_incomplete_sentence(response)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
