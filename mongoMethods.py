from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
from bson.objectid import ObjectId

    
def mongoInsertDataMethod(insert,collection_name):
        """method to insert data into mongo"""
            
        ## Updated local connection string
        localConnString = "mongodb://localhost:27017"
        # Create a new client and connect to the server
        client =MongoClient(localConnString, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        db = client["challenges"]
        # Create the collection
        collection = db[collection_name]
        #pass in the ChatGPT response
        collection.insert_one(insert)
        print("insertion to mongoDB successful")
        client.close()

    
    

  
def getAllMongo(collection_name):  
        """method to gather all mongo data  """  
        localConnString = "mongodb://localhost:27017"
        # Create a new client and connect to the server
        client =MongoClient(localConnString, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        db = client["challenges"]
        # Create the collection/use existing collection
        collection = db[collection_name]


        #Gathering info from mongo collection
        cursor  = collection.find()
        all_data_string = ""
        for document in cursor :
        # Convert ObjectIds to strings before serializing
         document = {key: str(value) if isinstance(value, ObjectId) else value for key, value in document.items()}
         json_string = json.dumps(document, indent=4)
         all_data_string += json_string + "\n"
         client.close()
        return all_data_string#return all data     
    
