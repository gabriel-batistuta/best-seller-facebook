import uvicorn
from fastapi import FastAPI 
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer origem acesse o recurso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def get_data():
    with open('db.json', 'r') as file:
        data = json.load(file)
    return data['data']

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)