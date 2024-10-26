from ai.aliy_tyqw_ai import sample_call_streaming
from ai.xf_starfire_ai import sample_starfire_call_streaming

class ChatConfig:
    def __init__(self, api_url: str = "", app_id: str = "", api_key: str = "", api_secret: str = "",
                 llm_domain: str = "", streaming: bool = False, prompt: str = "", model_name:str = "星火模型"):
        self.api_url = api_url
        self.app_id = app_id
        self.api_key = api_key
        self.api_secret = api_secret
        self.llm_domain = llm_domain
        self.streaming = streaming
        self.prompt = prompt
        self.model_name = model_name

def call_model(chatConfig):
    if chatConfig.model_name == "星火模型":
        return call_starfire_model(chatConfig)
    elif chatConfig.model_name == "通义千问模型":
        return call_tongyi_model(chatConfig)
    else:
        raise ValueError("未知的模型名称")

def call_starfire_model(chatConfig):
    response = sample_starfire_call_streaming(chatConfig.prompt,
                                              chatConfig.app_id,
                                              chatConfig.api_key,
                                              chatConfig.api_secret)
    return response

def call_tongyi_model(chatConfig):
    response = sample_call_streaming(chatConfig.prompt, api_key=chatConfig.api_key)
    return response

    #if response.status_code == 200:
    #    return response.json()
    #else:
    #    return None