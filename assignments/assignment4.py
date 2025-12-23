# Pricing Rule Engine 
total_electronics = 0
total_clothing = 0
total_grocery = 0
n = int(input("Enter number of items: "))
for i in range(n):
    print("\nItem", i + 1)
    category = input("Enter category (electronics/clothing/grocery): ").lower()
    price = float(input("Enter item price: "))
    # Input validation
    if price <= 0:
        print("Invalid price. Skipping item.")
        continue
    # Discount rules
    if category == "electronics":
        discount = price * 0.10
        final_price = price - discount
        total_electronics += final_price
    elif category == "clothing":
        discount = price * 0.20
        final_price = price - discount
        total_clothing += final_price
    elif category == "grocery":
        discount = price * 0.05
        final_price = price - discount
        total_grocery += final_price
    else:
        print("Invalid category. Skipping item.")
        continue
    print("Final price after discount:", final_price)
# summery
print("\n---- CATEGORY TOTALS ----")
print("Electronics Total:", total_electronics)
print("Clothing Total:", total_clothing)
print("Grocery Total:", total_grocery)
