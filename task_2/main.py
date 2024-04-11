from database import get_database
from crud_operations import create_cat, read_all_cats, read_cat_by_name, update_cat_age, update_cat_features, delete_cat_by_name, delete_all_cats

# Main function
def main():
    # Get database connection
    db = get_database()

    if db is not None:
        # Perform CRUD operations

        # Create a new cat
        create_cat(db, "Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
        create_cat(db, "Tom", 7, ["актор", "виводить мишей", "сірий"])
        create_cat(db, "Simba", 2, ["спритний", "любит лазити", "золотистий"])
        create_cat(db, "Misty", 4, ["спокійна", "любит сидіти на підвіконні", "чорна"])
        create_cat(db, "Fluffy", 1, ["грайливий", "пухнастий", "білий"])

        # Read all cats
        read_all_cats(db)

        # Read a cat by name
        read_cat_by_name(db, "Barsik")

        # Update cat's age
        update_cat_age(db, "Barsik", 4)

        # Update cat's features
        update_cat_features(db, "Barsik", "лагідний")

        # Delete cat by name
        delete_cat_by_name(db, "Barsik")

        # Delete all cats
        delete_all_cats(db)

if __name__ == "__main__":
    main()
