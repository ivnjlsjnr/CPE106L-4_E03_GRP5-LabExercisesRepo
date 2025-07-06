from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

CONNECTION_STRING = "mongodb://localhost:27017/"

DATABASE_NAME = "Chinook" 
ARTISTS_COLLECTION_NAME = "artists"
ALBUMS_COLLECTION_NAME = "albums"
TRACKS_COLLECTION_NAME = "tracks"

def connect_to_mongodb():
    try:
        client = MongoClient(CONNECTION_STRING)
   
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")
        return client
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        print("Please ensure MongoDB server is running and accessible.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during connection: {e}")
        return None

def main():
    client = connect_to_mongodb()
    if not client:
        return

    try:
        # Get a reference to the database
        db = client[DATABASE_NAME]
        print(f"Connected to database: {db.name}")

        # --- Example: Interacting with the 'artists' collection ---
        artists_collection = db[ARTISTS_COLLECTION_NAME]

        # --- Insert an Artist (if not already exists) ---
        # We'll check if an artist with _id: 1 already exists to avoid duplicates
        existing_artist = artists_collection.find_one({"_id": 1})
        if not existing_artist:
            artist_document = {
                "_id": 1,
                "Name": "AC/DC"
            }
            artists_collection.insert_one(artist_document)
            print("Inserted AC/DC into artists collection.")
        else:
            print("AC/DC already exists in artists collection.")

        # --- Find and Print all Artists ---
        print("\nArtists in the collection:")
        for artist in artists_collection.find({}):
            print(artist)

        # --- Example: Interacting with the 'albums' collection ---
        albums_collection = db[ALBUMS_COLLECTION_NAME]

        # --- Insert an Album (if not already exists) ---
        existing_album = albums_collection.find_one({"_id": 1})
        if not existing_album:
            album_document = {
                "_id": 1,
                "Title": "For Those About To Rock We Salute You",
                "ArtistId": 1 # Link to AC/DC
            }
            albums_collection.insert_one(album_document)
            print("Inserted 'For Those About To Rock We Salute You' into albums collection.")
        else:
            print("'For Those About To Rock We Salute You' already exists in albums collection.")

        # --- Find and Print all Albums ---
        print("\nAlbums in the collection:")
        for album in albums_collection.find({}):
            print(album)

        # --- Example: Interacting with the 'tracks' collection ---
        tracks_collection = db[TRACKS_COLLECTION_NAME]

       
    
        print("\nTracks in the collection:")
        for track in tracks_collection.find({}):
            print(track)

        print("\nOperations completed successfully.")

    finally:
        # Ensure the client connection is closed
        if client:
            client.close()
            print("MongoDB connection closed.")

if __name__ == "__main__":
    main()
