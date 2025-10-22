from database import get_connection

#product seaction

def add_product(name:str,price:float,quantity: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO products(name, price, quantity) VALUES(? ,? ,? )",
        (name, price, quantity)
    )
    conn.commit()
    conn.close()
    print("Product added successfully")

def get_all_prodects():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM products')
    row = cur.fetchall()
    conn.close()
    return row

def update_product_price(product_name: str, new_price: float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('UPDATE products SET price = ? WHERE name = ?',(new_price,product_name))
    conn.commit()
    conn.close()

def delete_prodect(prodect_id:int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM products WHERE id = ?',(prodect_id,))

    conn.commit()
    conn.close()
    print("Product deleted successfully")


#supliers seaction

def add_suppliers(name:str,phone:int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('INSERT INTO suppliers (name,phone) VALUES(?,?)', (name,phone))

    conn.commit()
    conn.close()
    print("suppliers added successfully")

def update_suppliers(supliers_id:int,new_supliers:str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('UPDATE suppliers SET name = ? WHERE id = ?',(new_supliers,supliers_id))

    conn.commit()
    conn.close()
    print("suppliers updated successfully")

def delete_suppliers(suppliers_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM suppliers WHERE id = ?',(suppliers_id,))
    conn.commit()
    conn.close()
    print("suppliers deleted successfully")

def get_all_suppliers():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM suppliers')
    row = cur.fetchall()

    conn.commit()
    conn.close()
    return row


def add_purchase(product_id:int, supplier_id:int, quantity:int, cost_price:float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('INSERT INTO purchases (product_id,supplier_id,quantity,cost_price) VALUES(?,?,?,?)',(product_id,supplier_id,quantity,cost_price))
    cur.execute('UPDATE products SET quantity = quantity + ? WHERE id = ?',(quantity, product_id))

                
    conn.commit()
    conn.close()
    print("Purchase added and stock updated")


#supliers seaction
def add_sale(product_id: int, quantity: int, selling_price: float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('INSERT INTO sales (product_id,quantity,selling_price) VALUES(?,?,?)',(product_id,quantity,selling_price))
    cur.execute('UPDATE products SET quantity = quantity - ? WHERE id = ?',(quantity, product_id))

    conn.commit()
    conn.close()
    print("Sale recorded and stock reduced")


#AI seaction
def get_low_stock_products(threshold: int = -498):
     conn = get_connection()
     cur = conn.cursor()

     cur.execute("""
        SELECT id, name, price, quantity
        FROM products
        WHERE quantity <= ?
        ORDER BY quantity ASC
    """, (threshold,))
     
     row = cur.fetchall()
     conn.close()
     return row


def get_top_selling_products(limit: int = 5):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT products.id, products.name, SUM(sales.quantity) AS total_sold
        FROM sales
        JOIN products
        ON sales.product_id = products.id
        GROUP BY products.id, products.name
        ORDER BY total_sold DESC
        LIMIT ?
    """, (limit,))

    row = cur.fetchall()
    conn.close()
    return row


def get_product_history(product_id: int):
    conn = get_connection()
    cur = conn.cursor()

    print("\nPurchase History:")
    cur.execute("""
        SELECT quantity, cost_price, purchase_date
        FROM purchases
        WHERE product_id = ?
        ORDER BY purchase_date DESC
    """,(product_id,))

    for row in cur.fetchall():
        print(f"  +{row['quantity']} (cost {row['cost_price']}) on {row['purchase_date']}")

    print("\nSales History:")
    cur.execute("""
        SELECT quantity, selling_price, sale_date
        FROM sales
        WHERE product_id = ?
        ORDER BY sale_date DESC
    """, (product_id,))
    for row in cur.fetchall():
        print(f"  -{row['quantity']} (price {row['selling_price']}) on {row['sale_date']}")

    conn.close()

