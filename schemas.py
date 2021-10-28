from pydantic import BaseModel
from typing import Optional


class InAnalyseString(BaseModel):
    string: str
    substring: Optional[str] = None


class OutAnalyseString(BaseModel):
    lower_case_letters_count: int
    upper_case_letters_count: int
    digits_count: int
    special_characters_count: int
    substring_occurrences_count: Optional[int]
