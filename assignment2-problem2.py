annual_salary = float(input("What is your annual salary? $"))
performance_score = float(input("What is your performance score (0-100)? "))

if performance_score >= 90:
    bonus_percent = 20
elif performance_score >= 80:
    bonus_percent = 10
elif performance_score >= 70:
    bonus_percent = 5
else:
    bonus_percent = 0

bonus_amount = annual_salary * (bonus_percent / 100)

print(f"Performance Bonus: {bonus_percent}%")
print(f"Bonus Amount: ${bonus_amount:,.2f}")