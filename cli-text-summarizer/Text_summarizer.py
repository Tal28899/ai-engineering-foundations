import groq
from groq import Groq
import time  

def text_summarizer(prompt:str,client,max_retries=3,waittime =5):
    "Function that calls grok api and genrate response and handles all types of error."
    last_error = None
    
    messages = [{"role": "system", "content":"""You are a expert summary writer. extract valid points from the prompt/
                and write a bullet point summary.Keep the summary as short as possible."""},
               {"role":"user", "content" : prompt}
            ]
    
    for attempts in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages = messages,
                temperature = 0.2,
                max_tokens = 1000,
                model="openai/gpt-oss-120b"
            )
            if not chat_completion.choices:
                print("Server Issue response is not generated.")
                return None
            
            response = chat_completion.choices[0].message.content
            
            if not response or not response.strip():
                print("Server Issue empty summary.")
                return None
            
            return (response)

        except groq.AuthenticationError:
            print(" API key is missing or invalid. check .env file.")
            return None

        except groq.RateLimitError as e:
            last_error = "Rate limit hit"
            retry_after = e.response.headers.get("retry-after")
            wait_time = float(retry_after) if retry_after else waittime * (2 ** attempts)
            print(f" Rate limit hit.Wait for {wait_time}s...(attempt{attempts+1}/{max_retries})")
            time.sleep(wait_time)

        except groq.APIConnectionError:
            print("Check your internet connection.")
            return None
            
        except groq.APITimeoutError:
            print("Request timed out!.")
            return None

        except groq.APIStatusError as e:
            print(e.status_code)
            print(e.message)
            return None

        except Exception as e:
            print(f"something unexpected happens: {e}")
            return None

    print(last_error)
    return None       
