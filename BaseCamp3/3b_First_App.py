from fastapi import FastAPI
import uvicorn
import time
from datetime import datetime

app = FastAPI()

# End Point definition with a GET method
@app.get("/welcome")
def welcome (name : str):
    """
    GET /welcome : Takes name as input
    Returns a welcome message
    """

    return "Welcome "+str(name)+". This is your first FastAPI app ...!"

# End Point definition with a GET method
# This function simulates a delay
@app.get("/test")
def test ():
    """
    Simulates a delay and return a string
    """
    st = datetime.now ()
    time.sleep (5)
    en = datetime.now ()

    return "Entry : "+str(st)+" | Exit : "+str(en)

# Uvicorn startup block
if __name__ == "__main__":
    uvicorn.run(
        "3b_First_App:app",
        host="0.0.0.0",
        port=5600,
        reload=True
    )
