from pymongo import MongoClient, errors

# Function to establish a connection to MongoDB
def get_database():
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb+srv://chivapchichi:Hn94Jfqq@chivapchichi.nrvpa6f.mongodb.net/?retryWrites=true&w=majority&appName=chivapchichi")
        db = client['cat_database']
        print("Connected to the database.")
        return db
    except errors.ConnectionError as e:
        print(f"Connection error: {e}")
        return None
