import psycopg2
import enviroment
import os

HOST = os.environ.get('host')
DBNAME = os.environ.get('dbname')
USER = os.environ.get('user')
PASSWORD = os.environ.get('password')
PORT = os.environ.get('port')

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(f"host={HOST} dbname={DBNAME} user={USER} password={PASSWORD} port={PORT}")
    
    def getAllProducts(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM products ORDER BY name DESC")
        result = cur.fetchall()
        cur.close()
        return result
    
    def addProduct(self, productName, productPrice):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO products (name, price) VALUES('{productName}', {productPrice})")
        self.connection.commit()
        cur.close()
        return

    def deleteProduct(self, productId):
        cur = self.connection.cursor()
        cur.execute(f"DELETE FROM products p WHERE p.id = {productId}", productId)
        self.connection.commit()
        cur.close()
        return
    