from fastapi import APIRouter, HTTPException
from app.services.translation_service import TranslationService

router = APIRouter()
translation_service = TranslationService()

@router.post("/")
async def translate(text: str, model_name: str = "model_1"):
    try:
        translated_text = translation_service.translate(text, model_name)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
