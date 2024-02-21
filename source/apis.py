# apis.py
from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from source.services import TextExtractionService

router = APIRouter()

@router.post("/extract_text")
async def extract_text(image: UploadFile):
    try:
        image_data = await image.read()
        extracted_text = TextExtractionService.extract_text_from_image(image_data)
        return JSONResponse(content={"text": extracted_text}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": f"Internal Server Error: {str(e)}"}, status_code=500)
        