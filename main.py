from fastapi import FastAPI, Depends
import schemas
import services
import dependencies

app = FastAPI()


@app.get(path="/analyse-string", response_model=schemas.OutAnalyseString)
async def analyse_string(request: schemas.InAnalyseString, analyser: services.StringService = Depends(dependencies.string_analyser)):
    ...
