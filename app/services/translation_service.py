from app.models.model_1 import Model1
from app.models.model_2 import Model2
from app.api.utils.preprocess import preprocess
from app.api.utils.postprocess import postprocess

class TranslationService:
    def __init__(self):
        self.models = {
            "model_1": Model1("models_data/model_1/model_1.pth"),
            "model_2": Model2("models_data/model_2/model_2.pth"),
        }

    def translate(self, text: str, model_name: str) -> str:
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Invalid model name: {model_name}")

        preprocessed_text = preprocess(text)
        translated_text = model.translate(preprocessed_text)
        postprocessed_text = postprocess(translated_text)

        return postprocessed_text
