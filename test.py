from chatbot import get_ai_response

print("Testing Groq chatbot...")

message = "Hello! Introduce yourself in one short sentence."

reply = get_ai_response(message)

print("Bot:", reply)
