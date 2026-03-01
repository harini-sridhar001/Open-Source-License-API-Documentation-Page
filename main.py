from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI(
    title="OSLI - Open Source License Intelligence API",
    description="Stateful SPDX compliance engine powered by Gemini AI.",
    version="1.0.0",
)

@app.get("/", response_class=HTMLResponse)
async def homepage():
    path = Path(__file__).parent / "docs" / "index.html"
    return HTMLResponse(content=path.read_text(), status_code=200)