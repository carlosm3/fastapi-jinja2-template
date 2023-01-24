from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Import routes
# from app.routes import user, auth

# Register routes
# app.include_router(user.router)
# app.include_router(auth.router)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


""" 
    Run uvicorn dev server
    uvicorn main:app --reload

    Install dependencies
    pip install -r requirements.txt
"""