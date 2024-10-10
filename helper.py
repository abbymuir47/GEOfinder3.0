import chromadb
import numpy as np
import pandas as pd
import web_app
from web_app import data_frame
   
#returns a dataframe, filtered based on the user's selections
def filter_by_metas(metadata_dct):
    global data_frame
    df_copy = data_frame.copy(deep=True) 


    #filtering the dataframe copy based on experiment type
    if(metadata_dct["Experiment_Type"]):
        if(len(metadata_dct["Experiment_Type"])==1):
            if(metadata_dct["Experiment_Type"][0]=="Microarray"):
                df_copy = df_copy[df_copy["Experiment_Type"].str.startswith("Expression profiling by array")]
            elif(metadata_dct["Experiment_Type"][0]=="RNA sequencing"):
                df_copy = df_copy[df_copy["Experiment_Type"].str.endswith("Expression profiling by high throughput sequencing")]
        
    #filtering the dataframe copy based on number of samples
    if(metadata_dct["Num_Samples"]):
        #add selected sample numbers to dataframe
        #df_copy = df_copy[df_copy["Samples_Range"] in metadata_dct["Num_Samples"]]
        df_copy = df_copy[df_copy["Samples_Range"].isin(metadata_dct["Num_Samples"])]
    
    #filter by years
    df_copy["Year_Released"] = pd.to_numeric(df_copy["Year_Released"], errors='coerce')
    df_copy = df_copy[(df_copy["Year_Released"] >= int(metadata_dct["Years"][0])) & (df_copy["Year_Released"] <= int(metadata_dct["Years"][1]))]
    return df_copy

#returns a dictionary of the closest results to the user IDs input
def generate_id_query_results(input_ids):

    chroma_client = chromadb.PersistentClient(path="./collectionFiles")
    my_collection = chroma_client.get_collection(name="geo_collection")
    
    input_embeddings = []

    for id in input_ids:
        print("in for loop, id:", id)
        data_dict = my_collection.get(ids=id, include=["embeddings"])
        print("data_dict: ", data_dict)
        print("length of embeddings:", len(data_dict["embeddings"]))
        input_embeddings.append(data_dict["embeddings"][0])


    input_embeddings = np.array(input_embeddings)
    avg_embedding = np.mean(input_embeddings, axis=0).tolist()

    num_results = 50
    # similarityResults = my_collection.query(query_embeddings=avg_embedding, n_results=num_results)
    similarityResults = my_collection.query(query_embeddings=avg_embedding, n_results=num_results)
    #print(f"\n\nSimilarity Results: {similarityResults}\n")
    return similarityResults["ids"][0]

#returns a list of all GSE ID's in the filtered_AllGEO.tsv file 
def generate_database_ids():
    database_ids = []
    with open("filtered_AllGEO.tsv", "r") as filtered_file:
        line1 = filtered_file.readline()
        for line in filtered_file:
            items = line.split("\t")
            database_ids.append(items[0])
    return database_ids
