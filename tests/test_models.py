from app.models.model_1 import Model1
from app.models.model_2 import Model2

def test_model_1():
    model = Model1("models_data/model_1/model_1.pth")
    assert model.translate("Hello world!") == "Translated text"

def test_model_2():
    model = Model2("models_data/model_2/model_2.pth")
    assert model.translate("Hello world!") == "Translated text"
