import litellm


class ModelRunner:
    def __init__(self, model_name: str, url: str = "",
                 max_tokens: int = 4096, temperature: float = 0.2) -> None:
        self.model_name = model_name
        self.url = url
        self.max_tokens = max_tokens
        self.temperature = temperature

    def run(self, prompt: dict):
        messages = [
            {"role": "system", "content": prompt['system']},
            {"role": "user", "content": prompt['user']}
        ]

        completion_params = {
            "model": self.model_name,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "stream": True,
            "temperature": self.temperature,
        }

        if self.url != "":
            completion_params["api_base"] = self.url

        response = litellm.completion(**completion_params)