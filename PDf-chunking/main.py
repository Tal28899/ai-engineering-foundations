import chromadb
from chunking import fixed_chunk,recurrsive_splitter,sentence_chunk
from text_extracter import extract_text
from input import taking_input
from llm import chat,groq_client
from embeddings import embeddings_storage,chromadb_client

def main():
    #Extracting text and making chunks
    data = extract_text("C:/Users/nn/Downloads/sample_notes.pdf")

    # Making different types of chunks
    f_chunks = fixed_chunk(data)
    s_chunks = sentence_chunk(data)
    r_chunks = recurrsive_splitter(data)

    # Creating a chromadb,groq clients
    g_client = groq_client()
    ch_client = chromadb_client()

    # Taking input from the user
    query = taking_input()
    if not query:
        print("No query provided. Exiting.")
        exit()

    # making and stroing embeddings
    results = embeddings_storage(ch_client,s_chunks=s_chunks,f_chunks=f_chunks,r_chunks=r_chunks,query=query)

    responses = []
    for i,result in enumerate(results):
        # prompt
        prompt = f"""
            You are a ai assitant bot that only give ansewer from the Context given below in <context> tags.
            .If the answer is not in the context then say so.
            You will be given query of the user in <query> tags.
            This is context :
            <context>
            {" ".join(result)}
            </context>
            This is the user query:
            <query>
            {query}
            </query>
            analyze and think before answering."""

        response = chat(prompt,g_client)
        if response:
            responses.append(response)
    paragraph_res,sentence_res,recursive_res =responses
    print("Fixed Chunking Response: ",paragraph_res)
    print()
    print("Sentence Chunking Response: ",sentence_res)
    print()
    print("Recursive Chunking Response: ",recursive_res)

if __name__ == "__main__":
    main()
            