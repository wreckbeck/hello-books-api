
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, name):
        self.name = name

planets = [
    Planet("Saturn"),
    Planet("Earth"),
    Planet("Mars")
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

#GET ALL
@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "name": planet.name
        })
    return jsonify(planets_response)


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Lord of the Rings", "A fantasy novel about a really cool ring."),
    Book(2, "Lord of the Flies", "A fictional novel about angry children."),
    Book(3, "Children of the Corn", "A fictional novel about scary corn kids.")
] 
books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)