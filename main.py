from fastapi import FastAPI, Depends
import schemas
import services
import dependencies

app = FastAPI()


@app.post(path="/analyse-string", response_model=schemas.OutAnalyseString)
async def analyse_string(request: schemas.InAnalyseString, analyser: services.StringService = Depends(dependencies.string_analyser)):
    """ Analyses given string """
    result = analyser.analyse(request.string, request.substring)
    return schemas.OutAnalyseString(
        digits_count=result.digits_count,
        lower_case_letters_count=result.lower_case_letters_count,
        upper_case_letters_count=result.upper_case_letters_count,
        special_characters_count=result.special_characters_count,
        substring_occurrences_count=result.substring_occurrences_count,
    )
