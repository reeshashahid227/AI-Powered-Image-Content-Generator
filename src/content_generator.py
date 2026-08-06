import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def generate_custom_captions(
    caption,
    style,
    tone,
    language,
    num_captions
):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")

    client = Groq(api_key=api_key)

    prompt = f"""
You are an AI content writer.

Original Image Caption:
{caption}

Style:
{style}

Tone:
{tone}

Language:
{language}

Generate {num_captions} different captions.

Requirements:
- Every caption should be unique.
- Keep captions concise.
- Keep captions relevant to the image.
- Follow the selected style.
- Follow the selected tone.
- Write completely in {language}.
- Return ONLY the captions.
- Number them from 1.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()