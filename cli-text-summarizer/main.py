from input_handler import taking_input
from huge_doc_summarizer import count_tokens,long_doc_summarizer,chunk_text,client
from Text_summarizer import text_summarizer

def main():
    # taking input from the user
    text_to_summarize= taking_input()
    if text_to_summarize:
        if count_tokens(text_to_summarize) > 8000:
           chunks = chunk_text(text_to_summarize)
           summary = long_doc_summarizer(chunks)
        else:
            summary = text_summarizer(text_to_summarize,client=client)   

        return summary
    else:
        return None    
    

if __name__ == "__main__":
    results = main()
    if results:
        print(results) 
                         