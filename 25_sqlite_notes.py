"""Distinct Python example #25."""
import sqlite3
with sqlite3.connect("notes.db") as db:
 db.execute("CREATE TABLE IF NOT EXISTS notes(body TEXT)"); db.execute("INSERT INTO notes VALUES (?)",("example note",)); print(db.execute("SELECT body FROM notes").fetchall())
