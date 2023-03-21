import torch

class BaseModel:
    def __init__(self, model_path: str):
        self.model = torch.load(model_path)

    def translate(self, text: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")
