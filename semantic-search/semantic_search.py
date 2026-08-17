import numpy as np
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from typing import Optional

# loading the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# data for retrival
sentences = [
    "Ahmad likes watching TV in the evening.",
    "Umer enjoys using his phone at night.",
    "Fatima always cries after waking up.",
    "Ali plays cricket every weekend with his friends.",
    "Sara loves reading novels before sleeping.",
    "The football match was postponed due to heavy rain.",
    "Cricket fans were disappointed when the tournament got cancelled.",
    "I need to buy groceries from the market today.",
    "She went to the supermarket to purchase vegetables.",
    "The weather in Lahore is extremely hot this summer.",
    "It has been raining continuously in Karachi this week.",
    "He is learning Python programming for his career.",
    "Web development requires knowledge of HTML, CSS, and JavaScript.",
    "My favorite hobby is painting landscapes on weekends.",
    "The new smartphone has an amazing camera and battery life."
]

def taking_input()->Optional[str]:
    "Taking input from the user"    
    try:  
        query = input("What you want to ask : ").strip()
        if not query:
            raise ValueError("Your question is empty.")
        elif len(query) <= 12:
            raise ValueError("Ask a complete question.")

    except ValueError as e:
        print(e)
        return None
    return query


query = taking_input()
if query is not None:

    # Making data and query embeddings
    d_embeddings = model.encode(sentences)
    q_embedding = model.encode(query)

    # list for storing similar results
    sim_results = []

    # Similarity search
    for i,d_embedding in enumerate(d_embeddings):
        sim = cos_sim(q_embedding,d_embedding)
        sim_results.append((sim,sentences[i]))

    #Sorting to get the top similar results
    ordered_sim_results= sorted(sim_results, key = lambda x:x[0],reverse=True)

    # printing the top 2 similar searches
    for sim,sentence in ordered_sim_results[0:3]:
        print(sim,sentence)









