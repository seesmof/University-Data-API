import os


current_dir: str = os.path.dirname(os.path.abspath(__file__))


class Constants:
    BASE_DIR: str = os.path.join(current_dir, "..")
    API_DIR: str = os.path.join(BASE_DIR, "api")
    TEST_DIR: str = os.path.join(BASE_DIR, "test")
    DATA_DIR: str = os.path.join(BASE_DIR, "data")

    API_URL: str = "https://unidata.vercel.app"
