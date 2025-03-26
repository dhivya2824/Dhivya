import csv
from difflib import get_close_matches

def load_data(file_path):
    books = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            if len(row) >= 3:
                books.append((row[1], row[2], row[3]))  # (Title, Author, Publisher)
    return books

def recommend_books(book_title, books, top_n=5):
    titles = [book[0] for book in books]
    similar_titles = get_close_matches(book_title, titles, n=top_n, cutoff=0.4)
    return similar_titles if similar_titles else "No similar books found."

# Load dataset
books = load_data(r"c:\Users\balaj\Downloads\Books system.csv")

# Example Usage
book_name = "Classical Mythology"
print("Recommended books:", recommend_books(book_name, books))
