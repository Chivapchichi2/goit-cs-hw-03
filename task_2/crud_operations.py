from bson.objectid import ObjectId

# Create a new document (adding a new cat)
def create_cat(db, name, age, features):
    try:
        cat_collection = db['cats']
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        cat_collection.insert_one(cat)
        print(f"Cat '{name}' added to the database.")
    except Exception as e:
        print(f"Error creating cat: {e}")

# Read all documents in the collection
def read_all_cats(db):
    try:
        cat_collection = db['cats']
        cats = cat_collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error reading all cats: {e}")

# Read a cat by name
def read_cat_by_name(db, name):
    try:
        cat_collection = db['cats']
        cat = cat_collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"No cat found with name '{name}'.")
    except Exception as e:
        print(f"Error reading cat by name: {e}")

# Update cat's age by name
def update_cat_age(db, name, new_age):
    try:
        cat_collection = db['cats']
        result = cat_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Updated age of cat '{name}' to {new_age}.")
        else:
            print(f"No cat found with name '{name}'.")
    except Exception as e:
        print(f"Error updating cat age: {e}")

# Update cat's features by name
def update_cat_features(db, name, new_feature):
    try:
        cat_collection = db['cats']
        result = cat_collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Added feature '{new_feature}' to cat '{name}'.")
        else:
            print(f"No cat found with name '{name}'.")
    except Exception as e:
        print(f"Error updating cat features: {e}")

# Delete a cat by name
def delete_cat_by_name(db, name):
    try:
        cat_collection = db['cats']
        result = cat_collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Deleted cat with name '{name}'.")
        else:
            print(f"No cat found with name '{name}'.")
    except Exception as e:
        print(f"Error deleting cat: {e}")

# Delete all cats
def delete_all_cats(db):
    try:
        cat_collection = db['cats']
        result = cat_collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats.")
    except Exception as e:
        print(f"Error deleting all cats: {e}")
