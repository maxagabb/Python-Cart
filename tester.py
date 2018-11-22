import db
import sqlite3
from business import Product, LineItem, Cart

conn = sqlite3.connect("products2.sqlite")
c = conn.cursor()

for line in open("products.sql"):
    c.execute(line)



if conn:
    conn.close()