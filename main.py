from fastapi import FastAPI

app = FastAPI()    #instancia que permite que todo el framework funcione, con el constructor se crea un objeto de tipo fastAPI y se guarda dentro de app -> es esta variable la que nos permite correr un proyecto

@app.get("/")
def home():
    return {"Hello": "World"}