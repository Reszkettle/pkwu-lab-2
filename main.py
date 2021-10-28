from fastapi import FastAPI
import schemas

app = FastAPI()


@app.get(path="/analyse-string", response_model=schemas.OutAnalyseString)
async def analyse_string(request: schemas.InAnalyseString):
    ...
