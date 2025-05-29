from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os

app = FastAPI(title="Dermato AI")

# In-memory storage for emails
waitlist = []

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/submit-email")
async def submit_email(email: str = Form(...)):
    try:
        # Store email in memory
        waitlist.append({
            "email": email,
            "timestamp": datetime.utcnow()
        })
        return {"message": "Successfully joined the waitlist!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to submit email")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 