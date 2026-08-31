import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

user_pdf_path = input("Enter path to your PDF file: ").strip()
#PDF ke naam se ek unique folder-naam banao:
pdf_name = os.path.basename(user_pdf_path)   # "resume.pdf"
pdf_name_clean = os.path.splitext(pdf_name)[0]  # "resume" (extension hata di)
PERSIST_DIR = f"chroma_db_{pdf_name_clean}"   # "chroma_db_resume"
    

# Step 1: Embedding function (needed whether we build or load the vectorstore)
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 2: Load existing vectorstore if available, else build a new one
if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
    print("Existing vector store found. Loading it...")
    try:
        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embedding_function
        )
    except Exception as e:
        print(f"Error loading existing vector store: {e}")
        exit()
else:
    print("No existing vector store found. Building a new one...")

    # Load PDF
    try:
        loader = PyPDFLoader(user_pdf_path)
        documents = loader.load()
        
    except ValueError:
        print("Error: The PDF file is empty or could not be read.")
        exit()
    except Exception as e:
        print(f"Error loading PDF: {e}")
        exit()

    # Split into chunks
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,       # small chunks for more precise retrieval
            chunk_overlap=49,     # slight overlap to preserve context across chunk boundaries
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(documents)
    except Exception as e:
        print(f"Error splitting documents: {e}")
        exit()

    # Embed and store chunks
    try:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_function,
            persist_directory=PERSIST_DIR
        )
    except Exception as e:
        print(f"Error creating vector store: {e}")
        exit()

# Step 3: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# Step 4: Set up LLM
try:
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    )
except Exception as e:
    print(f"Error setting up LLM: {e}")
    exit()

# Step 5: Prompt template
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the following context.
If the answer is not in the context, say "I don't know based on the given document."

Context:
{context}

Question: {input}
""")

# Step 6: Q&A loop
print("\nPDF Q&A Bot ready. Type 'quit' to exit.\n")

while True:
    query = input("Ask a question: ").strip()
    if query.lower() == "quit":
        break
    if not query:
        continue

    try:
        results = retriever.invoke(query)
        context = "\n".join(chunk.page_content for chunk in results)
        final_prompt = prompt.invoke({"context": context, "input": query})
        response = llm.invoke(final_prompt)
        print(response.content, "\n")
        
    except Exception as e:
        print(f"Error answering question: {e}\n")
        continue