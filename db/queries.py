CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""

INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_ORDER_TABLE = """
    CREATE TABLE IF NOT EXISTS order_product (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    size VARCHAR(255),
    product_id VARCHAR(255),
    amount_products VARCHAR(255),
    phone_number VARCHAR(255)
    )
"""

INSERT_ORDER_PRODUCTS = """
    INSERT INTO order_product ( size, product_id, amount_products, phone_number)
    VALUES (?, ?, ?, ?)
"""