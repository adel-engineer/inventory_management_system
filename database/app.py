
from models import (
    add_product, get_all_prodects, update_product_price, delete_prodect,
    add_suppliers, get_all_suppliers, delete_suppliers,
    add_purchase, add_sale,
    get_low_stock_products, get_top_selling_products, get_product_history
)


def line():
    print("-" * 60)

def pause():
    input("\nPress Enter to continue...")

def menu():
    while True:
        line()
        print("Inventory Management System")
        line()
        print("1) Add New Product")
        print("2) Show All Products")
        print("3) Update Product Price")
        print("4) Delete Product")
        print("5) Add Supplier")
        print("6) Show All Suppliers")
        print("7) Purchase Product (Increase Stock)")
        print("8) Sell Product (Reduce Stock)")
        print("9) Report: Low Stock Products")
        print("10) Report: Top Selling Products")
        print("11) Report: Product History (Purchase/Sales)")
        print("0) Exit")
        line()

        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                qty = int(input("Enter quantity: "))
                add_product(name, price, qty)
                pause()

            elif choice == "2":
                products = get_all_prodects()
                for p in products:
                    print(dict(p))
                pause()

            elif choice == "3":
                product_name = input("Enter product name: ")
                new_price = float(input("Enter new price: "))
                update_product_price(product_name, new_price)
                pause()

            elif choice == "4":
                product_id = int(input("Enter product ID: "))
                delete_prodect(product_id)
                pause()

            elif choice == "5":
                name = input("Enter supplier name: ")
                phone = input("Enter phone number (optional): ") or None
                add_suppliers(name, phone)
                pause()

            elif choice == "6":
                suppliers = get_all_suppliers()
                for s in suppliers:
                    print(dict(s))
                pause()

            elif choice == "7":
                pid = int(input("Enter product ID: "))
                sid = int(input("Enter supplier ID: "))
                qty = int(input("Enter purchased quantity: "))
                cost = float(input("Enter cost price: "))
                add_purchase(pid, sid, qty, cost)
                pause()

            elif choice == "8":
                pid = int(input("Enter product ID: "))
                qty = int(input("Enter sold quantity: "))
                price = float(input("Enter selling price: "))
                add_sale(pid, qty, price)
                pause()

            elif choice == "9":
                print("\nLow Stock Products:")
                for row in get_low_stock_products():
                    print(dict(row))
                pause()

            elif choice == "10":
                print("\nTop Selling Products:")
                for row in get_top_selling_products():
                    print(dict(row))
                pause()

            elif choice == "11":
                pid = int(input("Enter product ID: "))
                get_product_history(pid)
                pause()

            elif choice == "0":
                print("Exiting the system. Thank you for using the program.")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            pause()


if __name__ == "__main__":
    menu()
