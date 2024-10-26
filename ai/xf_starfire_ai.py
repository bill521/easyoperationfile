from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage


def sample_starfire_call_streaming(prompt, spark_app_id, spark_api_key, spark_api_secret, spark_llm_domain="generalv3", spark_api_url="wss://spark-api.xf-yun.com/v3.1/chat"):
    SPARKAI_URL = spark_api_url
    SPARKAI_DOMAIN = spark_llm_domain
    completion = SparkAICommunicator(SPARKAI_URL, spark_app_id, spark_api_key, spark_api_secret, SPARKAI_DOMAIN)
    result = completion.communicate_with_ai(prompt)
    return result

class SparkAICommunicator:
    def __init__(self, spark_api_url, spark_app_id, spark_api_key, spark_api_secret, spark_llm_domain):
        self.spark = ChatSparkLLM(
            spark_api_url=spark_api_url,
            spark_app_id=spark_app_id,
            spark_api_key=spark_api_key,
            spark_api_secret=spark_api_secret,
            spark_llm_domain=spark_llm_domain,
            streaming=False,
        )

    def communicate_with_ai(self, message_content: str):
        messages = [ChatMessage(role="user", content=message_content)]
        handler = ChunkPrintHandler()
        response = self.spark.generate([messages], callbacks=[handler])
        print(response)
        return response.generations[0][0].text


