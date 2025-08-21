from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def test(request: Request):
    print((await request.body()).decode("utf-8"))
    return {"Hello": "World"}

