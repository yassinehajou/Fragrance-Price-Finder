import psycopg2
from cityrhythm_scraper import scrape_cityrhythm

hostname = 'localhost'
database = 'cityrhythm'
username = 'postgres'
pwd = 'admin'
port_id = 5432

# intialize connection and cursor before using them to avoid errors
conn = None
cur = None

def insert_products(products): 
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id)
        
        print("Connected to the database")      
        cur = conn.cursor()

        cur.execute("DROP TABLE IF EXISTS products;")
        create_script = ''' CREATE TABLE products (
                                    id              SERIAL PRIMARY KEY,
                                    title           varchar(255) NOT NULL,
                                    image_url       text NOT NULL,
                                    link            text NOT NULL,
                                    sale_price      DECIMAL(10,2),
                                    original_price  DECIMAL(10,2),
                                    from_price      DECIMAL(10,2),
                                    category        VARCHAR(255) NOT NULL,
                                    is_on_sale      BOOLEAN NOT NULL
                            ); '''        
        cur.execute(create_script)
        conn.commit()

        insert_script = ''' INSERT INTO products (title, image_url, link, sale_price, original_price, from_price, category, is_on_sale)
                            VALUES (DEFAULT, %(title)s, %(image_url)s, %(link)s, %(sale_price)s, %(original_price)s, %(from_price)s, %(category)s, %(is_on_sale)s); '''
        
        default_values = {
            'sale_price': None,
            'original_price': None,
            'from_price': None,
            'category': 'Unknown', 
            'is_on_sale': False
        }

        for product in products:
            # Update product dictionary with default values for missing keys
            for key, value in default_values.items():
                product.setdefault(key, value)

            cur.execute(insert_script, product)
        conn.commit()

        cur.execute("SELECT * FROM products;")
        print(cur.fetchall())

    except Exception as e:
        print(f"An error occured: {e}")
        raise
    
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:    
            conn.close()

def main():
    product_data = scrape_cityrhythm()
    insert_products(product_data)

if __name__ == "__main__":
    main()