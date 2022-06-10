from project.app.routers import auth, users

from fastapi import FastAPI, status


app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health", status_code=status.HTTP_200_OK, )
async def health():
    return {"message": "successful launch"}
