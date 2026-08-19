from Text_summarizer import text_summarizer
import tiktoken
import time
import os
from groq import Groq
from dotenv import load_dotenv
# loading the enviroment variable
load_dotenv()

# Storing API key in a variable
api_key =os.getenv("GROQ_API_KEY")

client = Groq(api_key = api_key)
def count_tokens(text)->int:
    """Function for counting the no of tokens"""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))
     

def chunk_text(text,max_token_limit=7000)-> list:
    """It takes a huge documnets and break down it into chunks"""
    encoding = tiktoken.get_encoding("cl100k_base")
    words = text.split()
    chunks =[]
    current_chunk = []
    current_tokens = 0
    for word in words:
        words_t =len(encoding.encode(word + " "))
        if current_tokens + words_t > max_token_limit:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_tokens = words_t
        else:
            current_tokens += words_t
            current_chunk.append(word)
    # Appending the last Chunk
    if current_chunk:
            chunks.append(" ".join(current_chunk))
    return chunks
             
def long_doc_summarizer(text)->str:
    """It finds each individual chunk summary.
        Then is appends each invidual summary  in chunk_summary.
        After that it calculates the summary of chunk_summary
        and gives the final complete summary."""
    chunk_summary = []
    for chunk in text:
        chunk_summary.append(text_summarizer(chunk.strip(),client=client))
        time.sleep(60)
    chunk_summary = [chunk.strip() for chunk in chunk_summary if chunk]
    if chunk_summary:    
        complete_s = text_summarizer("\n\n".join(chunk_summary),client=client)
        return complete_s
    else:
        return None    
