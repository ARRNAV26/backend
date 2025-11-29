from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class AutocompleteRequest(BaseModel):
    code: str
    cursorPosition: int
    language: str

class AutocompleteResponse(BaseModel):
    suggestion: str

@router.post("", response_model=AutocompleteResponse)
async def get_autocomplete(request: AutocompleteRequest) -> AutocompleteResponse:
    # Mocked suggestions based on the language
    suggestions = {
        "python": [
            "def ",
            "class ",
            "import ",
            "print(",
            "if __name__ == '__main__':"
        ]
    }

    language = request.language.lower()
    if language not in suggestions:
        raise HTTPException(status_code=400, detail="Unsupported language")

    # Return the first suggestion as a mock
    suggestion = suggestions[language][0]
    return AutocompleteResponse(suggestion=suggestion)
