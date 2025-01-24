# TODO: Login. (Optional)
# TODO: Add multiple reviews/comments to a book. (Optional)
# TODO: Search for specific book reviews with a certain rating. (Optional)
# TODO: Add author's name to a book. (Optional)
# TODO: Filter reviews by rating

import csv


HEADERS = ['name', 'rating', 'comments']


def main():

    print("Welcome to our reviews system!")

    while True:

        # Display the menu
        print("1. List all reviews.")
        print("2. Add a review.")
        print("3. Edit a review.")
        print("4. Delete a review.")
        print("5. Exit.")
    
        # Get the user's choice
        choice = get_input("Enter your choice: ")

        # Perform the chosen action
        if choice == "1":
            list_reviews()
        elif choice == "2":
            add_review()
        elif choice == "3":
            edit_review()
        elif choice == "4":
            delete_review()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def list_reviews():
    """List all reviews in the database."""

    database = load_database()

    if len(database) == 0:
        print("Database is empty.")
        print()
    
    else:
        # Print each review
        print("Name | Rating | Comments")
        print("-------------------------")
        for review in database:
            print(f"{review['name']} | {review['rating']} | {review['comments']}")
        print(f"Total reviews: {len(database)}\n")


def edit_review():
    """Edits a review in the database."""

    database = load_database()

    name = get_existing_name("Enter the name of the review you want to edit: ")
    new_rating = get_rating("Enter the new rating (1-5): ")
    new_comments = get_input("Enter the new comments: ")

    with open('database.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, HEADERS)
        writer.writeheader()
        for review in database:
            if review['name'] == name:
                review['rating'] = new_rating
                review['comments'] = new_comments
                writer.writerow(review)
            else:
                writer.writerow(review)
                
    print(f"Review for {name} has been updated.\n")


def add_review():
    """Add a review to the database."""

    name = get_new_name("Enter the name of the item: ")
    rating = get_rating("Enter the rating (1-5): ")
    comments = get_input("Enter your comments: ")

    with open('database.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, HEADERS)
        writer.writerow({
            'name': name, 
            'rating': rating, 
            'comments': comments
        })

    print(f"Review for {name} has been added.\n")


def delete_review():

    database = load_database()

    name = get_existing_name("Enter the name of the item you want to delete: ")

    with open('database.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, HEADERS)
        writer.writeheader()

        for review in database:
            if review['name'] != name:
                writer.writerow(review)

    print(f"Review for {name} has been deleted.\n")


def load_database():
    """Returns a list of dictionaries, representing the list of reviews."""
    
    with open('database.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
    

def get_input(prompt):
    """Prompts the user for input, ensuring the input is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_new_name(prompt):
    """Prompts the user for a new name."""
    database = load_database()
    while True:
        name = str(get_input(prompt))
        if any(item['name'] == name for item in database):
            print("Book already exists.")
        else:
            return name
        

def get_existing_name(prompt):
    """Prompts the user for an existing name."""
    database = load_database()
    while True:
        name = get_input(prompt)
        if not any(item['name'] == name for item in database):
            print("Book not found.")
        else:
            return name


def get_rating(prompt):
    """Prompts the user for a valid rating."""
    rating = get_input(prompt)
    if not rating.isdigit() or not 1 <= int(rating) <= 5:
        print("Please enter a valid rating! (1-5): ")
        return get_rating(prompt)
    return int(rating)


if __name__ == "__main__":
    main()
