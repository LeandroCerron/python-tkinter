import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect("host=localhost dbname=test user=root password=123456 port=5432")
    
    def getAllProducts(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM products ORDER BY name DESC")
        result = cur.fetchall()
        cur.close()
        print(result)
        return result
    
    def addProduct(self, productName, productPrice):
        cur = self.connection.cursor()
        cur.execute(f"INSERT INTO products (name, price) VALUES('{productName}', {productPrice})")
        self.connection.commit()
        cur.close()
        return
    
    def connections(self):
        cur = self.connection.cursor()
        cur.execute("select * from pg_stat_activity where datname = 'test'")
        result = cur.fetchall()
        print(len(result))
        return