
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

AIVEN_PASSWORD = os.getenv("AIVEN_PASSWORD")

print("Using Aiven password:", AIVEN_PASSWORD) 

class Shopee:

    def add_product(self, category_id, product_name, description, price, stock_quantity, image_url, is_featured):
        conn = pymysql.connect(host='mysql-mithil-23-python-mysql-23.h.aivencloud.com' ,port=21763, user='avnadmin',password=AIVEN_PASSWORD, database='shopee')
        
        query = """
        INSERT INTO products 
        (category_id, product_name, description, price, stock_quantity, image_url, is_featured) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        with conn.cursor() as cursor:
            cursor.execute(query, (
                category_id,
                product_name,
                description,
                price,
                stock_quantity,
                image_url,
                is_featured
            ))
        conn.commit()
        conn.close()
        print(str)
        flag=True
        return flag
    
    def show_category(self):
        con = pymysql.connect(host="mysql-mithil-23-python-mysql-23.h.aivencloud.com", port=21763, user="avnadmin", password=AIVEN_PASSWORD, database="shopee")
        curs = con.cursor()
        qr = f'select * from products'
        curs.execute(qr)
        data = curs.fetchall()
        con.close()
        return data
    
    def show_product(self):
        con = pymysql.connect(host="mysql-mithil-23-python-mysql-23.h.aivencloud.com", port=21763, user="avnadmin", password=AIVEN_PASSWORD, database="shopee")
        curs = con.cursor()
        qr = f'select * from products'
        curs.execute(qr)
        data = curs.fetchall()
        con.close()
        return data

    def delete_product(self, product_id):
        conn = pymysql.connect(host="mysql-mithil-23-python-mysql-23.h.aivencloud.com", port=21763, user="avnadmin", password=AIVEN_PASSWORD, database="shopee")
        curs = conn.cursor()
        curs.execute("delete from products WHERE product_id = %s", (product_id,))
        conn.commit()
        curs.close()
        curs.close()


    

