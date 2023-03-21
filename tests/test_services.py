from app.services.translation_service import TranslationService

def test_translation_service():
    service = TranslationService()
    assert service.translate("Hello world!", "model_1") == "Translated text"
    assert service.translate("Hello world!", "model_2") == "Translated text"
