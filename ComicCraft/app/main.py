from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
import urllib.parse

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

# Template folder rendu edathulayum check pannum
if (BASE_DIR / "templates").exists():
    t_dir = str(BASE_DIR / "templates")
else:
    t_dir = str(BASE_DIR.parent / "templates")
templates = Jinja2Templates(directory=t_dir)

def get_image(text):
    # safe URL
    q = urllib.parse.quote(text[:120])
    return f"https://image.pollinations.ai/prompt/{q}?width=512&height=512&nologo=true"

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/generate")
async def gen(request: Request):
    try:
        form = await request.form()
        story = str(form.get("story_prompt") or "A brave cat")
        char = str(form.get("character_name") or "Cat Hero")
        setting = str(form.get("setting") or "Chennai")
        tone = str(form.get("tone") or "funny")
        style = str(form.get("art_style") or "comic")

        base = f"{char} in {setting}, {story}, {tone}, {style}"

        panels = []
        for i, scene in enumerate([
            f"{base}, intro",
            f"{base}, problem",
            f"{base}, action fight",
            f"{base}, sad struggle",
            f"{base}, happy ending"
        ], 1):
            panels.append({
                "title": f"Panel {i}",
                "image": get_image(scene),
                "text": scene
            })
        
        return templates.TemplateResponse(request, "result.html", {"story": story, "panels": panels})
    except Exception as e:
        print("ERROR:", e)
        return templates.TemplateResponse(request, "result.html", {
            "story": f"Error: {e}",
            "panels": []
        })