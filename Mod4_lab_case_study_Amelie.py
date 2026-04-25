from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
books = []

# ----------------------
# CREATE a Book
# ----------------------
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    book = {
        "id": data["id"],
        "book_name": data["book_name"],
        "author": data["author"],
        "publisher": data["publisher"]
    }

    books.append(book)
    return jsonify({"message": "Book added successfully", "book": book}), 201


# ----------------------
# READ all Books
# ----------------------
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# ----------------------
# READ single Book by ID
# ----------------------
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404


# ----------------------
# UPDATE a Book
# ----------------------
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()

    for book in books:
        if book["id"] == book_id:
            book["book_name"] = data.get("book_name", book["book_name"])
            book["author"] = data.get("author", book["author"])
            book["publisher"] = data.get("publisher", book["publisher"])

            return jsonify({"message": "Book updated", "book": book})

    return jsonify({"message": "Book not found"}), 404


# ----------------------
# DELETE a Book
# ----------------------
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})

    return jsonify({"message": "Book not found"}), 404


# ----------------------
# Run Server
# ----------------------
if __name__ == '__main__':
    app.run(debug=True)