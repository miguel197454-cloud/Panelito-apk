import torch
import json
import random

from model import NeuralNet
from utils import bag_of_words, tokenize

device = torch.device('cpu')

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

data = torch.load("data.pth", map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(data["model_state"])
model.eval()


def get_response(message):
    sentence = tokenize(message)
    X = bag_of_words(sentence, all_words)
    X = torch.from_numpy(X).unsqueeze(0)

    output = model(X)
    probs = torch.softmax(output, dim=1)
    confidence, predicted = torch.max(probs, dim=1)

    tag = tags[predicted.item()]

    if confidence.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])

    return "No entendí 🤔"