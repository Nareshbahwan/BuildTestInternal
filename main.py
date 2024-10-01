from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
import json
from data_read import metro_overview_data_reader
import uvicorn
import os

app = FastAPI(
     title="MEDOS 360 API",
     description="API to be used for MEDOS360",
     default_response_class=ORJSONResponse
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return{'MEDOS 360 API'}

@app.get('/metro_overview_7_days_actual_test_json')
async def get_metro_details():
    json_file_path =r'D:\PythonCode\build_test\BuildTestInternal\data\metrodashboard.json'
    with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
    
    # data = metro_overview_data_reader.read_data()
    return JSONResponse(content=data)

@app.get('/metro_overview_7_days')
async def get_metro_details():

    output = metro_overview_data_reader.read_data()
  
    return output

if __name__ == '__main__':
    default_port = 8001
    try:
        port = int(os.environ.get('SERVER_PORT', str(default_port)))
    except:
        port = default_port
 
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info", reload=True, workers=None)