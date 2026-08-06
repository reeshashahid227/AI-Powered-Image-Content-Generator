import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def generate_custom_caption(
    caption,
    style,
    tone,
    language
):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env file."
        )

    client = Groq(api_key=api_key)

    prompt = f"""
You are an AI content writer.

Create a customized image caption based on the information below.

Original image caption:
{caption}

Caption style:
{style}

Tone:
{tone}

Language:
{language}

Requirements:
- Keep the caption relevant to the image.
- Follow the requested style.
- Follow the requested tone.
- Write entirely in the requested language.
- Keep it concise and natural.
- Do not explain your answer.
- Return only the final caption.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()