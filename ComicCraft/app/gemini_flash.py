import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")


def generate_outline(prompt, character_name, setting, tone, art_style):
    instruction = f"""
Create a structured 5-panel comic outline.

Story prompt: {prompt}
Main character: {character_name}
Setting: {setting}
Tone: {tone}
Art style: {art_style}

For each panel provide:
1. Panel number
2. Title
3. Scene description
4. Image generation prompt
"""

    response = model.generate_content(instruction)
    return response.text