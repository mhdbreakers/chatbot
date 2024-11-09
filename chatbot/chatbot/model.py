from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Charger le modèle GPT-2 et le tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Fonction pour générer une réponse
def generate_response(user_input):
    # Tokeniser l'entrée de l'utilisateur
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    
    # Décoder la réponse générée
    bot_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Retourner la réponse générée
    return bot_output
