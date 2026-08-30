# ---------------- WELCOME ----------------
print("🍽️ Swagatam to The Locals 🍽️")

# ---------------- MENU ----------------
Menu = {
    "Pizza": 120,
    "Momos": 80,
    "Samosa": 20,
    "Idli": 20,
    "Vada Pav": 30,
    "Soya Champ": 100,
    "White Sauce Pasta": 120,
    "Red Sauce Pasta": 130,
    "Ras Malai": 40,
    "Rabri": 30,
    "Gulab Jamun": 20
}

# ---------------- SHOW MENU ----------------
print("\n📜 Menu:")
for item, price in Menu.items():
    print(f"{item} : Rs{price}")

# ---------------- ORDER SYSTEM ----------------
total = 0   # store total bill
cart={}
import difflib
while True:
    item = input("\nEnter item (or 'done'): ").title()

    # Exit condition
    if item == "Done":
        break
    

    # Check item availability
    # if item in Menu:
    #     price = Menu[item]
    #     total = total + price
    #     print(f"✅ {item} added. Price = Rs{price}")
    # else:
    #     print("❌ Item not available")  My old code to item availability 

# new for check item
    if item in Menu:
        qty = int(input("Enter quantity: "))   # ✅ ask quantity

        cart[item] = cart.get(item, 0) + qty   # ✅ store in cart

        price = Menu[item]
        total = total + (price * qty)          # ✅ multiply
        print(f"✅ {item} x{qty} added. Price = ₹{price * qty}")
    else:
        print("❌ Item not available")
    


    

# ---------------- FINAL BILL ----------------
# print("\n------ BILL ------")
# print(f"Total Bill = Rs{total}")
# print("------------------")

# print("\n🙏 Thank you! Visit again.")

print("\n🛒 Your Cart:")
for item, qty in cart.items():
    price = Menu[item]
    print(f"{item} x{qty} = ₹{price * qty}")

print("------------------")
print(f"Total Bill = ₹{total}")