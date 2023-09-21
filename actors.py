from openai_api import call_openai
from gensim.models import Word2Vec
import numpy as np
import random
import json
import os

# Load actor memory from file or initialize
if os.path.exists("actor_memory.json"):
    with open("actor_memory.json", "r") as f:
        actor_memory = json.load(f)
else:
    actor_memory = {}

model = Word2Vec(sentences=[["hello", "world"]], vector_size=100, window=5, min_count=1, sg=0)  # Dummy Word2Vec model

def text_to_vector(text):
    words = text.split()
    vectors = [model.wv[word] for word in words if word in model.wv]
    if not vectors:
        vectors = [np.random.rand(100)]  # Handle unknown words
    return np.mean(vectors, axis=0)

def generate_lines(actor_type, scene, director_notes):
    if actor_type not in actor_memory:
        actor_memory[actor_type] = np.random.rand(100).tolist()  # Initialize memory with random numbers
    
    prompt = f"A {actor_type} actor with a certain style influenced by past performances is about to perform the following scene: {scene}. Director's notes: {director_notes}"
    
    line = call_openai(prompt)
    if line.startswith("Error"):
        return line
    
    # Update actor memory
    update_vector = text_to_vector(f"{director_notes} {line}")
    actor_memory[actor_type] = (np.array(actor_memory[actor_type]) + update_vector).tolist()
    
    # Save updated memory to file
    with open("actor_memory.json", "w") as f:
        json.dump(actor_memory, f)
    
    return line
