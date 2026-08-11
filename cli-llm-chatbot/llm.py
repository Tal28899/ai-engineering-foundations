from groq import Groq,RateLimitError,APIError,APIConnectionError
import os
from dotenv import load_dotenv


# loading environment variable
load_dotenv()

# Getting the API key from environment variables
api_key = os.getenv("GROQ_API_KEY") or os.getenv("API_Key") or os.getenv("API_KEY")

#setting vales for message list and client
message = [
        {"role": "system", "content": "You are my assistant."},
    ]
client = Groq(api_key=api_key)

try:
    while True:
        user_input = input("Enter your prompt (or 'quit' to exit): ")
        if user_input.lower() == "quit":
            break
        user_input = {"role" : "user", "content": user_input}
        message.append(user_input)
        
        chat_completion = client.chat.completions.create(
            messages=message,
            model="llama-3.3-70b-versatile",
            temperature=0.1,
            max_tokens=1000
            )
        response = chat_completion.choices[0].message.content
        message.append({"role": "assistant", "content": response})
        print(response)
except APIConnectionError:
    print("No internet connection.")
except RateLimitError as e:
    print(f"Rate limit error: {e}")
except APIError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")    
