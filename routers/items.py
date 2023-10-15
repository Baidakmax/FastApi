from fastapi import APIRouter, BackgroundTasks
from starlette.responses import JSONResponse
from models.core import ItemFirst

router = APIRouter()

@router.get("/")
def items():
    return [
        {
            "id": 1,
            "name": "first"
        }
    ]


@router.get("/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, 'name': 'first'}



#
#
# def console_print():
#     for i in range(10):
#         print(i)
#
#
# @router.get('/task')
# def back_task(background_task: BackgroundTasks):
#     background_task.add_task(console_print)
#     return {'Run': "task"}
#
#
# @router.post("/item/{item_id}")
# async def create_item(item: ItemFirst, item_id: int):
#     return JSONResponse({"item": item.dict(), "item_id": item_id})
#
#
# @router.get("/item/{item_id}")
# async def get_item(item: ItemFirst, item_id: int):
#     return JSONResponse({"item_id": item_id})