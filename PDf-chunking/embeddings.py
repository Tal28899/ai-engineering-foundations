import chromadb

def chromadb_client():
    return chromadb.PersistentClient(path = "./my_chunks_vector")

def embeddings_storage(client,f_chunks,s_chunks,r_chunks,query)->list:
    """This Function Takes 3 Different Categories of Chunking. Makes Individual
        Collection And Retrive Results For Each Chunk."""

    # Making Collections For Each Chunking
    collection1 = client.get_or_create_collection(name = "paragraph_chunks")
    collection2 = client.get_or_create_collection(name = "sentences_chunks")
    collection3 = client.get_or_create_collection(name = "recurssive_chunks")

    #Storing Chunks In Collections If Not Already Stored
    if collection1.count() == 0:
        collection1.add(
            documents = f_chunks,
            ids = [f"fixed_chunk{i}" for i in range(len(f_chunks))],
            metadata = [{"docments_id": "1", "source": "sample_notes.pdf"} for _ in f_chunks]
        )

    if collection2.count() == 0:
        collection2.add(
            documents = s_chunks,
            ids = [f"s_chunk{i}" for i in range(len(s_chunks))],
            metadata = [{"docments_id" : "1" ,"source" : "sample_notes.pdf"} for _ in s_chunks]
        )

    if collection3.count() == 0:
        collection3.add(
            documents = r_chunks,
            ids = [f"r_chunk{i}" for i in range(len(r_chunks))],
            metadata = [{"docments_id" : "1" ,"source" : "sample_notes.pdf"} for _ in r_chunks]
        )

    #Retrived content by each chunk strategy based on the query 
    results1 = collection1.query(query_texts = [query],n_results = 2)
    r1 = results1["documents"][0]

    results2 = collection2.query(query_texts = [query],n_results = 2)
    r2 = results2["documents"][0] 

    results3 = collection3.query(query_texts = [query],n_results = 2)
    r3 = results3["documents"][0]

    # Storing retrived content of each Chunking strategy and returning it in a list.
    return [r1,r2,r3]
