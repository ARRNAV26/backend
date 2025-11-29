from typing import Dict, Any

def get_mocked_autocomplete_suggestion(code: str, cursor_position: int, language: str) -> Dict[str, Any]:
    # Mocked suggestions based on simple rules
    suggestions = {
        "python": [
            "def ",
            "class ",
            "import ",
            "print(",
            "if __name__ == '__main__':",
            "for ",
            "while ",
            "return ",
            "try:",
            "except:",
        ]
    }
    
    # Return a simple suggestion based on the last word typed
    last_word = code[:cursor_position].split()[-1] if cursor_position > 0 else ""
    
    # Filter suggestions based on the last word
    filtered_suggestions = [s for s in suggestions.get(language, []) if s.startswith(last_word)]
    
    return {"suggestions": filtered_suggestions}