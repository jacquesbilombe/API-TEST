import json
import string

def trans_data(input):
    if isinstance(input, str):
        raw = json.loads(input)
    
    if isinstance(raw, dict):
        text = raw.get("text").lower()
        used_language = raw.get("language") if raw else "english"
    
    tokenized = text.translate(str.maketrans("","", string.punctuation)).split(" ")
    
    return {
        "text": tokenized,
        "count": len(tokenized),
        "has_digit": any(char.isdigit() for char in tokenized),
        "language": used_language
    }