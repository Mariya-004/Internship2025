import chromadb

#creating a new database

chroma_client = chromadb.Client()

# creating a new collection

collection = chroma_client.create_collection(name="my_collection")

# adding documents to the collection
collection.add(
    documents=["Hello world", "Goodbye world"],
    ids=["id1", "id2"]
)

#querying the collection
results = collection.query(
    query_texts=["Hello world"],
    n_results=2
)
print(results)

#to save the data in a file

client = chromadb.PersistentClient(path="chroma_db")
print("Heartbeat:",client.heartbeat()) #heartbeat to keep the database alive

