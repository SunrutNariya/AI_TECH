# Product Catalog
catalog = {
    "apple": 30,
    "banana": 10,
    "milk": 50,
    "bread": 40,
    "eggs": 60
}

cart = []

def add_to_cart(*items):
    for item in items:
        if item in catalog:
            cart.append({"name": item, "price": catalog[item]})
            print(f"{item} added to cart.")
        else:
            print(f" {item} is not available.")

def remove_from_cart(item_name):
    for item in cart:
        if item["name"] == item_name:
            cart.remove(item)
            print(f"🗑️ {item_name} removed from cart.")
            return
    print(f" {item_name} not found in cart.")

def view_cart():
    if not cart:
        print("🛒 Cart is empty.")
        return
    print("\n🛒 Your Cart:")
    total = 0
    for idx, item in enumerate(cart, 1):
        print(f"{idx}. {item['name']} - ₹{item['price']}")
        total += item['price']
    print(f"Total: ₹{total}\n")

def checkout(**kwargs):
    total = sum(item['price'] for item in cart)
    discount = kwargs.get('discount', 0)
    tax = kwargs.get('tax', 0.05)  # default 5%
    
    print(f"Subtotal: ₹{total}")
    total -= total * discount
    total += total * tax
    print(f"Discount: {discount*100}%")
    print(f"Tax: {tax*100}%")
    print(f"Final Amount: ₹{round(total, 2)}")

# CLI Interface
print(" Welcome to SmartCart CLI System!")
while True:
    print("\n1. View Catalog\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        print("\n Catalog:")
        for item, price in catalog.items():
            print(f"- {item}: ₹{price}")
    elif choice == '2':
        items = input("Enter items to add (comma separated): ").split(',')
        add_to_cart(*[i.strip().lower() for i in items])
    elif choice == '3':
        item = input("Enter item to remove: ").strip().lower()
        remove_from_cart(item)
    elif choice == '4':
        view_cart()
    elif choice == '5':
        checkout(discount=0.10, tax=0.08)
        break
    elif choice == '6':
        print(" Thanks for shopping with us!")
        break
    else:
        print(" Invalid choice.")
