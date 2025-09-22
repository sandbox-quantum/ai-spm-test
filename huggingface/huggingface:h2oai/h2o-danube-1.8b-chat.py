from transformers.pipelines import pipeline
import torch

pipe = pipeline("text-generation", model="h2oai/h2o-danube-1.8b-chat", device="cuda", torch_dtype=torch.bfloat16)

messages = [
    [
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."},]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Write a poem on Hugging Face, the company"},]
        },
    ],
]

output = pipe(messages, max_new_tokens=50)
