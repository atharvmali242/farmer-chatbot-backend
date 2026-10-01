from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file.")

client = Groq(api_key=api_key)

MODEL_NAME = "openai/gpt-oss-120b"


def get_ai_response(user_message: str) -> str:
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
