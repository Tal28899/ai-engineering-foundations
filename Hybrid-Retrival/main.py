import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings   # updated
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers.ensemble import EnsembleRetriever


# Step 1: Load PDF 
loader = PyPDFLoader("tesla_10k.pdf")
pages = loader.load()

#  Selecting  Business + Risk Factors sections (tables-free range)
selected_pages = pages[4:29]  # index 4 to 28 inclusive

# Clean extra whitespace (PDF justified-text artifact) ----------
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

for page in selected_pages:
    page.page_content = clean_text(page.page_content)


# Step 3: Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(selected_pages)

print(f"Total chunks created: {len(chunks)}")

# Step 4: Dense retriever (semantic) 
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)
dense_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Step 5: BM25 retriever (keyword) 
bm25_retriever = BM25Retriever.from_documents(chunks)
bm25_retriever.k = 5

# Step 6: Hybrid (Ensemble) retriever
hybrid_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, dense_retriever],
    weights=[0.5, 0.5]  # tune these based on query type
)

#  Step 7: Query and test 
def run_query(query, retriever, label):
    print(f"\n Search Type : {label}")
    results = retriever.invoke(query)
    for i, doc in enumerate(results, start=1):
        print(f"Result {i}:\n{doc.page_content[:300]}\n---")
    print(results[0])

if __name__ == "__main__":
    query = input("Enter your query: ")

    run_query(query, bm25_retriever, "BM25 Only")
    run_query(query, dense_retriever, "Dense Only")
    run_query(query, hybrid_retriever, "Hybrid (Ensemble)")

