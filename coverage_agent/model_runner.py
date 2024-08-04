"""
Runner class that runs llm inference with prompt and
returns the repsonse.
Class uses litellm to run the inference.
"""
import inspect
import litellm
import sys

from logger import cust_logger


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

    Examples:
        >>> runner = ModelRunner("gpt-3.5-turbo")
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

        filename, line_number, fname, _, _\
            = inspect.getframeinfo(sys._getframe(0))

        cust_logger.info("%s::%s::%s::%s - Prompt:\n%s" % (
            filename.split('/')[-1], __class__.__name__,
            fname, line_number, messages))

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
            cust_logger.error("%s::%s::%s::%s - %s" % (
                filename.split('/')[-1], __class__.__name__,
                fname, line_number, e))

        model_response = litellm.stream_chunk_builder(chunks=chunks,
                                                      messages=messages)

        return model_response.choices[0].message.content


c = ModelRunner("gpt-3.5-turbo")
c.run({"user": "person", "system": "This is my prompt."})
