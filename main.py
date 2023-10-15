import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.items import router as router_item
from routers.users import router as router_user



app = FastAPI()

app.include_router(
    router=router_item,
    prefix='/items'
)

app.include_router(
    router=router_user,
    prefix="/users"
)


origins = ["http://127.0.0.1:8000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    responce = await call_next(request)
    process_time = time.time() - start_time
    responce.headers['X-Process-Time'] = str(process_time)
    responce.headers['Custom-Header'] = 'test'
    return responce





if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)