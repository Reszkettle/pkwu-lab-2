from typing import Optional
import re
from dataclasses import dataclass


@dataclass
class AnalyseResult:
    lower_case_letters_count: int
    upper_case_letters_count: int
    digits_count: int
    special_characters_count: int
    substring_occurrences_count: Optional[int]


class StringService:

    def analyse(self, string: str, substring: Optional[str]) -> Optional[AnalyseResult]:

        if not string:
            return None

        special_characters_regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        lower_case_letters_count = 0
        upper_case_letters_count = 0
        digits_count = 0
        special_characters_count = 0

        for char in string:
            if char.isupper():
                upper_case_letters_count += 1
            elif char.islower():
                lower_case_letters_count += 1
            elif char.isdigit():
                digits_count += 1
            elif special_characters_regex.search(char):
                special_characters_count += 1

        result = AnalyseResult(lower_case_letters_count=lower_case_letters_count, upper_case_letters_count=upper_case_letters_count,
                               digits_count=digits_count, special_characters_count=special_characters_count)
        if substring:
            result.substring_occurrences_count = string.count(substring)

        return result
