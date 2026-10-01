import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-pro")


def generate_story(outline):
    instruction = f"""
Create a detailed comic story from the following 5-panel outline.

Include narration and character dialogue for each panel.

Comic outline:
{outline}
"""

    response = model.generate_content(instruction)
    return response.texts