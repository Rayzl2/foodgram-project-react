import re
from django.core.exceptions import ValidationError


def validate_username(res: str) -> str:
    
    if res.lower() == "me":
        raise ValidationError("Недопустимое имя пользователя!")
    
    regex = re.compile("[^a-zA-Z0-9_]+")
    
    if regex.search(res):
        raise ValidationError("Присутствуют недопустимые символы в поле username")
    
    return res
