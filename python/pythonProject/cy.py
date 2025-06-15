import json
import random
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

# Load intents data
with open("intents.json", "r") as file:
    intents = json.load(file)

# Preprocess data
patterns = []
responses = []
tags = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(intent["responses"])
        tags.append(intent["tag"])

# Tokenize and vectorize
vectorizer = CountVectorizer().fit_transform(patterns)
vectorizer_array = vectorizer.toarray()


def chatbot_response(user_input):
    # Preprocess user input
    user_input_clean = re.sub(r'[^\w\s]', '', user_input.lower())
    user_vector = CountVectorizer().fit(patterns).transform([user_input_clean]).toarray()

    # Calculate similarity
    similarity = cosine_similarity(user_vector, vectorizer_array)
    max_sim_index = similarity.argmax()

    if similarity[0][max_sim_index] > 0.5:  # Set a threshold
        response = random.choice(responses[max_sim_index])
    else:
        response = "I'm not sure about that. Could you clarify?"

    return response


# Run chatbot
print("Cybersecurity Chatbot: Hello! How can I help you with cybersecurity?")
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Cybersecurity Chatbot: Stay safe online! Goodbye!")
        break
    print("Cybersecurity Chatbot:", chatbot_response(user_message))
