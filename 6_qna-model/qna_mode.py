from pymilvus import connections, Collection
from transformers import AutoTokenizer, AutoModel, pipeline
import torch
import numpy as np

# Connect to Milvus
connections.connect("default", host="localhost", port="19530")

# Load the collection
collection_name = "n_cuda"
collection = Collection(collection_name)

# Load pre-trained model and tokenizer for embeddings
embedding_model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(embedding_model_name)
embedding_model = AutoModel.from_pretrained(embedding_model_name)

# Tokenize the query sentence
query_sentence = "What is Cuda?"
inputs = tokenizer(query_sentence, return_tensors="pt")

# Generate embedding
with torch.no_grad():
    outputs = embedding_model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).numpy()

# Define search parameters and search in Milvus
search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=query_embedding.tolist(),
    anns_field="embeddings",
    param=search_params,
    limit=10
)

# Retrieve context from search results
context = ""
for result in results[0]:
    # Assume result.id corresponds to a document ID or text snippet
    # Retrieve the actual text data from the Milvus collection
    # For this example, we use placeholder text
    context += result.entity.get("sentences") + " "


qa_model_name = "distilbert-base-uncased-distilled-squad"
nlp = pipeline("question-answering", model=qa_model_name, tokenizer=qa_model_name)

# Generate the answer
answer = nlp(question=query_sentence, context=context)

# Display the answer
print("Question:", query_sentence)
print("Answer:", answer["answer"])
print("Context:", context)
