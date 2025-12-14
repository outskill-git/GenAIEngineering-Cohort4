from fastapi import FastAPI

# Define an App
app = FastAPI()

@app.get("/")
def base ():
    return "My First API ..."