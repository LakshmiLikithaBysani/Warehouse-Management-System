print("📦 Warehouse Management System")

products = []

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Stock")
    print("5. Delete Product")
    print("6. Count Products")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))

        product = {
            "id": product_id,
            "name": name,
            "category": category,
            "quantity": quantity
        }

        products.append(product)

        print("✅ Product added successfully!")

    # View Products
    elif choice == "2":
        if len(products) == 0:
            print("❌ No products found.")
        else:
            print("\n📋 Product Details")
            print("--------------------------")

            for product in products:
                print("Product ID:", product["id"])
                print("Product Name:", product["name"])
                print("Category:", product["category"])
                print("Quantity:", product["quantity"])
                print("--------------------------")

    # Search Product
    elif choice == "3":
        search_id = input("Enter product ID to search: ")

        found = False

        for product in products:
            if product["id"] == search_id:
                print("\n✅ Product Found")
                print("Product ID:", product["id"])
                print("Product Name:", product["name"])
                print("Category:", product["category"])
                print("Quantity:", product["quantity"])

                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Update Stock
    elif choice == "4":
        update_id = input("Enter product ID: ")

        found = False

        for product in products:
            if product["id"] == update_id:
                new_quantity = int(input("Enter new quantity: "))

                product["quantity"] = new_quantity

                print("✅ Stock updated successfully!")
                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Delete Product
    elif choice == "5":
        delete_id = input("Enter product ID to delete: ")

        found = False

        for product in products:
            if product["id"] == delete_id:
                products.remove(product)

                print("✅ Product deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Count Products
    elif choice == "6":
        print("📦 Total Products:", len(products))

    # Exit
    elif choice == "7":
        print("Thank you for using Warehouse Management System! 📦")
        break

    else:
        print("❌ Invalid choice!")
