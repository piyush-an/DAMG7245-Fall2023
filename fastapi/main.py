import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class UserInput(BaseModel):
    state:str

def load_df():
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    df = pd.read_fwf(r"https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    df = df[df['ST'].notna()]
    return df

@app.get("/api/v1/healthcheck")
async def say_hello() -> dict:
    return {"message":"Ok"}

@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/api/v1/fetch_all_data")
def fetch_data() -> JSONResponse:
    df = load_df()
    return JSONResponse(content=df.to_dict(orient='records'))

@app.post("/api/v1/fetch_by_state")
def fetch_data(userinput: UserInput) -> JSONResponse:
    df = load_df()
    filtered_df = df[df['ST'] == userinput.state.upper()]
    return JSONResponse(content=filtered_df.to_dict(orient='records'))
