import dashscope
from openai import OpenAI


def sample_call_streaming(prompt, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", api_key="sk-2c16341f2d43422190f59ff1afea642e"):
    dashscope.api_key = api_key
    client = OpenAI(
        api_key=dashscope.api_key,
        base_url=base_url,
    )
    completion = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': prompt}]
    )
    return completion.choices[0].message.content