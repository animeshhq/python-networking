from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Test API",
    description="Meant for Learning"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "author": "Animesh",
        "title": "Getting Started with Python",
        "content": "Today I learned about lists, dictionaries, and loops.",
        "date_posted": "2026-02-20"
    },
    {
        "id": 2,
        "author": "Neo",
        "title": "Asyncio Basics",
        "content": "Asyncio helps run tasks concurrently using async and await.",
        "date_posted": "2026-02-19"
    },
    {
        "id": 3,
        "author": "Ayush",
        "title": "PostgreSQL Setup",
        "content": "Installed PostgreSQL and connected it with a client app.",
        "date_posted": "2026-02-18"
    }
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts})

@app.get("/api/posts")
def get_posts():
    return posts