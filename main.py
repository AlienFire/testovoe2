from fastapi import FastAPI

from app.api.routes import root_router

app = FastAPI()


app.include_router(root_router)

#@app.get("/user")
#async def read_user(name: str = None):
#    return {"message": f"Hello {name}!"}