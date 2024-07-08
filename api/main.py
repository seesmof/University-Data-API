import os
from fastapi import FastAPI

from api.constants import Constants

app = FastAPI()


@app.get("/")
def display_hint() -> str:
    return "Hallelujah thank YOU Jesus Christ our Holy Lord GOD Almighty"


@app.get("/time")
def return_time() -> dict:
    base_dir: str = Constants.DATA_DIR
    target_file: str = os.path.join(base_dir, "class_times.yml")

    with open(target_file, "r", encoding="utf-8") as file:
        data = file.read()

    return {"time": data}
