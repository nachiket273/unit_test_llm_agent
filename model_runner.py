"""
Runner class that runs llm inference with prompt and
returns the repsonse.
Class uses litellm to run the inference.
"""
import litellm

from logger import clogger


class ModelRunner:
    """
    Initialize the instance of ModelRunner class.

    Args:
        model_name(str): The name of model to be used.
        url(str): The base API url to be used.
                  Empty if not required.
        max_tokens(int): Maximum tokens to be returned
                         Default: 4096
        temperature(float): Parameter to control the
                            randomness of the output
                            Default: 0.2
        log_path(str): Log directory Path
    """
    def __init__(self, model_name: str, url: str = "",
                 max_tokens: int = 4096,
                 temperature: float = 0.2
                 ) -> None:
        self.model_name = model_name
        self.url = url
        self.max_tokens = max_tokens
        self.temperature = temperature


    def run(self, prompt: dict):
        messages = [
            {"role": "system", "content": prompt['system']},
            {"role": "user", "content": prompt['user']}
        ]

        clogger.info("Prompt:\n%s" %messages)

        completion_params = {
            "model": self.model_name,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "stream": True,
            "temperature": self.temperature,
        }

        if self.url != "":
            completion_params["api_base"] = self.url

        chunks = []

        try:
            response = litellm.completion(**completion_params)

            for chunk in response:
                chunks.append(chunk)

        except Exception as e:
            raise e

        model_response = litellm.stream_chunk_builder(chunks=chunks,
                                                      messages=messages)

        return model_response.choices[0].message.content
