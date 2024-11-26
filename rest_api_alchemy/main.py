import json
import os

import yaml
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Carica il modello e il tokenizer
model_name = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")


@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.json
    prompt = data.get("prompt", "")

    # Tokenizza e genera testo
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=100,
        temperature=0.7,
        num_return_sequences=1
    )

    # Decodifica e restituisci la risposta
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})


@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.json
    # in data/prompts/general, load the first element of the prompts json and use it

    prompts = load_prompts("general.json")
    prompt = prompts[0]['prompt'].replace("{text}", data.get("text", ""))

    # Tokenizza e genera testo
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=100,
        temperature=0.7,
        num_return_sequences=1
    )

    # Decodifica e restituisci la risposta
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})


def load_prompts(file_name):
    """Load prompts from a JSON or YAML file in the data/prompts directory."""
    base_path = os.path.join(os.path.dirname(__file__), "data/prompts")
    file_path = os.path.join(base_path, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file {file_name} not found in {base_path}")

    # Determine file type
    _, ext = os.path.splitext(file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        if ext == ".json":
            return json.load(file)["prompts"]
        elif ext in [".yaml", ".yml"]:
            return yaml.safe_load(file)["prompts"]
        else:
            raise ValueError(f"Unsupported file format: {ext}")


if __name__ == "__main__":
    app.run(debug=True)
