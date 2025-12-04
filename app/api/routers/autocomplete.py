from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random

from app.services.autocomplete_service import get_mocked_autocomplete_suggestion

router = APIRouter()

class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str

class AutocompleteResponse(BaseModel):
    suggestion: str

@router.post("", response_model=AutocompleteResponse)
async def get_autocomplete(request: AutocompleteRequest) -> AutocompleteResponse:
    language = request.language.lower()

    result = get_mocked_autocomplete_suggestion(request.code, request.cursorPosition, language)
    suggestions = result["suggestions"]

    if suggestions:
        suggestion = random.choice(suggestions)
    else:
        suggestion = ""  # No suggestion available

    return AutocompleteResponse(suggestion=suggestion)
