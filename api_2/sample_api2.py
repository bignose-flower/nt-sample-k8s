from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/")
def read_root():
    return {"message" : "Welcom Api Service2!"}

@router.get("/hello")
def read_hello():
    return {"message" : "Hello, world From Server2!"}

app.include_router(router, prefix="/svr2")