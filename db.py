import sys
import os
import sqlite3
from contextlib import closing

from business import Product, LineItem, Cart, Category

conn = None

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = "products2.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = HOME + "products2.sqlite"
        
        conn = conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        conn.row_factory = sqlite3.Row


def get_products():
    connect()
    query = '''SELECT *
               FROM PRODUCTS'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    products = []
    for row in results:
        products.append(make_product(row))
    return products

def getProductByID(product_id):
    connect()
    query = '''SELECT *
               FROM PRODUCTS WHERE Product_ID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (product_id,))
        result = c.fetchone()
    product = make_product(result)
    return product

def close():
    if conn:
        conn.close()

def make_category(row):
    return Category(row["Category_ID"], row["categoryName"])

def make_product(row):
    return Product(row["Pname"], row["price"], row["discountPercent"], row["img"], row["Product_ID"])

def get_categories():
    connect()
    query = '''SELECT Category_ID, Cname as categoryName
               FROM CATEGORY'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT Category_ID, Cname AS categoryName
               FROM CATEGORY WHERE Category_ID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None

def get_products_by_category(category_id):
    connect()
    query = '''SELECT Product_ID, Pname, price, discountPercent,
                      PRODUCTS.Category_ID as categoryID, img,
                      Cname as categoryName
               FROM PRODUCTS JOIN CATEGORY
                      ON PRODUCTS.Category_ID = CATEGORY.Category_ID
               WHERE PRODUCTS.Category_ID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()
    products = []
    for row in results:
        products.append(make_product(row))
    return products

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def add_movie(movie):
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

def delete_movie(movie_id):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        test = conn.commit()
        print("Test", test)
