from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def display_hint() -> str:
    return "Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty"
