

import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload



