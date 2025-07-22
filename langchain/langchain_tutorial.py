from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


model1 = init_chat_model("gpt-4o-mini", model_provider="openai")
model2 = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
# this init_chat_model structure is used in almost all models

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

response1 = model1.invoke(messages)
response2 = model2.invoke(messages)

