purchase_amount = float(input("Enter purchase amount: $"))
membership_status = input("Is the customer a member? (yes/no): ").strip().lower()

if membership_status == "yes":
    if purchase_amount >= 100:
        discount_percent = 15
    else:
        discount_percent = 5
else:
    if purchase_amount >= 150:
        discount_percent = 10
    else:
        discount_percent = 0

discount_amount = purchase_amount * (discount_percent / 100)
final_price = purchase_amount - discount_amount

print(f"Discount applied: {discount_percent}%")
print(f"Final price: ${final_price:.2f}")