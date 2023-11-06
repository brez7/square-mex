import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="upbeat-button-265722", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.4,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat()
response = chat.send_message("""EXPLAIN PYTHON""", **parameters)
print(f"Response from Model: {response.text}")