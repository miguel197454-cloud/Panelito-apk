import torch
import json
import random
import nltk

from model import NeuralNet
from utils import bag_of_words, tokenize

# asegurar recursos nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# cargar intents
with open('intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

# cargar modelo
FILE = "data.pth"
data = torch.load(FILE, map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(data["model_state"])
model.eval()

bot_name = "Panelito"

# 🔥 NUEVO: memoria y contexto
user_name = None
context = None

print("Escribe 'salir' para terminar\n")

while True:
    sentence = input("Tú: ")

    if sentence.lower() == "salir":
        print(f"{bot_name}: ¡Hasta luego! 💪")
        break

    # 🧠 DETECTAR NOMBRE (memoria básica)
    if "me llamo" in sentence.lower():
        user_name = sentence.lower().split("me llamo")[-1].strip().capitalize()
        print(f"{bot_name}: Mucho gusto, {user_name} 😄 ¿Te gusta hacer ejercicio?")
        continue

    # 🔁 CONTEXTO (mini conversación)
    if context == "tipo_ejercicio":
        if "casa" in sentence.lower():
            print(f"{bot_name}: ¡Genial! 🏠 Puedes empezar con rutinas básicas como sentadillas y flexiones.")
        elif "gimnasio" in sentence.lower():
            print(f"{bot_name}: Perfecto 💪 En el gimnasio puedes combinar máquinas y peso libre.")
        else:
            print(f"{bot_name}: Buena elección 👍 Lo importante es mantener la constancia.")
        
        context = None
        continue

    # procesamiento normal
    sentence_tokens = tokenize(sentence)
    X = bag_of_words(sentence_tokens, all_words)
    X = torch.from_numpy(X).unsqueeze(0).to(device)

    output = model(X)

    probabilities = torch.softmax(output, dim=1)
    confidence, predicted = torch.max(probabilities, dim=1)

    tag = tags[predicted.item()]

    # 🎯 RESPUESTA CON CONFIANZA
    if confidence.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])

                # 👤 personalización
                if user_name:
                    response = f"{user_name}, {response}"

                print(f"{bot_name}: {response}")

                # 🔁 activar contexto
                if tag == "inicio_deporte":
                    context = "tipo_ejercicio"
                    print(f"{bot_name}: ¿Prefieres entrenar en casa o en gimnasio?")

                break
    else:
        print(f"{bot_name}: No estoy seguro de entenderte 🤔 ¿puedes decirlo de otra forma?")