from flask import Flask, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)
# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-DHI1BR4\\SQLEXPRESS;'
    'DATABASE=LibraryDB;'
    'Trusted_Connection=yes;'
)

@app.route('/books')
def get_books():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")

    books = []
    for row in cursor.fetchall():
        books.append({
            "BookID": row.BookID,
            "Title": row.Title,
            "Author": row.Author,
            "Genre": row.Genre,
            "AvailableCopies": row.AvailableCopies
        })

    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)