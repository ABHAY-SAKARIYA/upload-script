from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize the text and convert to tensor
inputs = tokenizer("how are you", return_tensors="pt")

# Compute embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Take the embeddings of the [CLS] token (first token in the sequence)
embedding = outputs.last_hidden_state[:, 0, :].numpy()

print("Embedding:", embedding)
