from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return """
    <html><body style="font-family:Arial;padding:20px;">
    <h1>ComicCraft AI 🎨</h1>
    <form action="/generate" method="post">
        <p>Story: <input name="story" value="A cat saves Chennai"></p>
        <p>Character: <input name="character" value="Whiskers"></p>
        <button type="submit" style="padding:10px;background:blue;color:white;">Generate Comic</button>
    </form>
    </body></html>
    """

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request):
    form = await request.form()
    story = list(form.values())[0] if form else "Hero story"
    return f"""
    <html><body style="font-family:Arial;padding:20px;">
        <h1>Comic Ready! 🎉 - 5 Panels</h1>
        <h2>Story: {story}</h2>
        <div style="border:2px solid black;margin:10px;padding:10px;">Panel 1: Hero in Chennai</div>
        <div style="border:2px solid black;margin:10px;padding:10px;">Panel 2: Problem comes</div>
        <div style="border:2px solid black;margin:10px;padding:10px;">Panel 3: Fight</div>
        <div style="border:2px solid black;margin:10px;padding:10px;">Panel 4: Struggle</div>
        <div style="border:2px solid black;margin:10px;padding:10px;">Panel 5: Happy Ending!</div>
        <br><a href="/">Back</a>
    </body></html>
    """