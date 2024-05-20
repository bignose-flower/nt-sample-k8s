from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/")
def read_root():
    return {"message" : "Welcom Api Service1!"}

@router.get("/hello")
def read_hello():
    return {"message" : "Hello, world From Server 1!"}

app.include_router(router, prefix="/svr1")