from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Montar la carpeta donde está tu archivo 'index.html'
app.mount("/static", StaticFiles(directory=".", html=True), name="static")

@app.get("/nombres")
async def obtener_nombres():
    return ["Zerha", "Melek", "Azad"]

# Ruta principal que sirve el index.html
@app.get("/")
async def read_index():
    return {"message": "¡Bienvenido a mi API con FastAPI!"}
