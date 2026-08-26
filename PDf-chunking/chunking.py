import spacy

def fixed_chunk(data)->list:
    """Takes Text And Break Them Into Fixed Size(150) Chunks
        And Returns List Containing Chunks"""
    data_l = data.split()
    chunks = []
    start = 0
    end = 150
    last_index = len(data_l)

    while True:
        if start > last_index:
            break

        elif end > last_index:
            end = last_index
            chunk = data_l[start:end]
            chunks.append(" ".join(chunk))
            break    

        else:    
            chunk = data_l[start:end]
            chunks.append(" ".join(chunk))
            start = end
            end += 150
    return chunks


def sentence_chunk(data,max_chars=200)->list:
    """Sentence Chunking Takes Text And Break Them Into Chunks
        Using Spay And Returns List Containing Chunks"""
    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")
    doc = nlp(data)
    sentences = [sen.text.strip() for sen in doc.sents]
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > max_chars and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence if current_chunk else sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks        

def recurrsive_splitter(data, chunksize = 200, chunk_ovelap = 35)-> list:
    """Recursive Text Splitter Takes Text And Break Them Into Chunks
        In a Herarcical MannerAnd Returns List Containing Chunks"""
    separators = ["\n\n","\n"," ",""]

    def split_by_sep(text,seps):
        if not seps:
            return list(text)
        sep = seps[0]
        if sep == "":
            return list(text)
        else:
            pieces = text.split(sep)
            pieces = [p.strip() for p in pieces if p.strip()]
        return pieces

    def get_pieces(text,seps):
        pieces = split_by_sep(text,seps)
        results = []
        for piece in pieces:
            if len(piece) > chunksize and len(seps) > 1:
                results.extend(get_pieces(piece,seps[1:]))
            else:
                results.append(piece)
        return results

    splitted_d = get_pieces(data,separators)
    
    chunks = []
    current_chunk = ""
    for chunk in splitted_d:
        if len(current_chunk) + len(chunk) > chunksize and current_chunk:
            chunks.append(current_chunk.strip())
            overlaping_chars = current_chunk[-chunk_ovelap:] if chunk_ovelap else ""
            current_chunk =  overlaping_chars + " " + chunk
        else:    
            current_chunk += " " + chunk 

    if current_chunk:
        chunks.append(current_chunk.strip())        
    return chunks        




