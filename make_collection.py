import chromadb
import csv
import gzip

#creating our permanent chromadb collection, called geo_collection, and putting it inside of our collectionFiles folder
chroma_client = chromadb.PersistentClient(path="./collectionFiles")
geo_collection = chroma_client.create_collection(name="geo_collection")

with gzip.open("../gte-large.tsv.gz") as gse_emb_file:
    for line in gse_emb_file:
        
        line_items = line.decode().rstrip("\n").split("\t")
        gse = line_items[0]
        embedding = line_items[1:]

        # Convert to numbers using a list comprehension.
        embedding = [float(x) for x in embedding]

        geo_collection.add(
            embeddings = embedding,
            ids = gse
        )