from dummy_data import dummy_data
from pymongo import errors
from pymongo import MongoClient


def connectDB():
    connection_string = "mongodb+srv://Cluster48520:QmpkRmVZW3Rv@cluster48520.xztuyj1.mongodb.net/"
    client = MongoClient(connection_string)
    db = client.Cluster48520
    print("Connection established to your db")
    return db

def createCollection(db):
    try:
        collection_name = input("Enter the collection name: ")
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created successfully!")
        elif collection_name in db.list_collection_names():
            print("Collection already exists")
    except Exception as e:
        print("An error occured: ", e)


def insert_into_collection(db):
    collection_name = input("Enter the collection name: ")
    try: 
        collection = db[collection_name]
        name = input("Enter the name: ")
        review_message = input("Enter the review message: ")
        given_star = int(input("Enter the star rating: "))
        review_data = {
            'film_name': name,
            'review_message': review_message,
            'given_star': given_star,
        }
        result = collection.insert_one(review_data)
        print("Insertion successfully completed")
    except:
        print(f"Collection does not exist!!!!!!")

def read_all_data(db):
    collection_name = input("Enter the collection name: ")
    try:
        collection = db[collection_name]
        result = collection.find()
        for document in result:
            print(document)
    except:
        print(f"Collection does not exist!!!!!!")

def filter_data(db):

    try:
        # Ask user for the collection name
        collection_name = input("Enter the collection name: ")


        # Ask user for the attribute and value to filter
        attribute = input("Enter the attribute to filter: ")
        value = input(f"Enter the value for '{attribute}' to filter: ")

        # Access the specified collection
        collection = db[collection_name]

        # Define the filter query dynamically based on the attribute and value
        query = {attribute: value}

        # Use the find method to retrieve matching documents
        cursor = collection.find(query)

        # Convert your cursor to a list to operate over it
        result = list(cursor)

        # Print the matching documents
        if not result:
            print(f"No data found with {attribute} equal to '{value}'.")
        else:
            print("Filtered Data:")
            for document in result:
                print(document)

        # Return the whole result list
        return result

    except ValueError as e:
        print(f"Error: {e}")

def update_data(db):
    try:
        collection_name = input("Enter the collection name: ")
        collection = db[collection_name]
        film_name = input("Enter the film name to update: ")
        field_to_update = input("Enter 'review_message' or 'given_star' to update: ")
        if field_to_update not in ['review_message', 'given_star']:
            raise ValueError("Invalid field to update")
        updated_data = input(f"Enter updated {field_to_update} for the film: ")
        
        query = {"film_name":film_name }

        # Use the update_one method to update the specific field (order_list)
        collection.update_one(query, {"$set": {field_to_update: updated_data}})


        print(f"Film {field_to_update} updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def delete_data(db):
    try:
        collection_name = input("Enter the collection name: ")
        collection = db[collection_name]
        film_name = input("Enter the film name to delete: ")
        collection = db[collection_name]
        query = {"film_name": film_name}
        collection.delete_many(query)

        print(f"document(s) deleted successfully!")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    db = connectDB()
    while True:
        print("\nWelcome to Review Portal!")
        print("1- Create a collection.")
        print("2- Read all data in a collection.")
        print("3- Read some part of the data while filtering.")
        print("4- Insert data.")
        print("5- Delete data.")
        print("6- Update data.")
        print("7- Quit")

        choice = input("Select an option: ")

        if choice == '1':
            createCollection(db)
        elif choice == '2':
            read_all_data(db)
        elif choice == '3':
            filter_data(db)
        elif choice == '4':
            insert_into_collection(db)
        elif choice == '5':
            delete_data(db)
        elif choice == '6':
            update_data(db)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
