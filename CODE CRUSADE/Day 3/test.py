name = input("Enter your name: ")
hours = int(input("Enter total hours worked: "))
rate = float(input("Enter hourly rate of pay: "))

base_pay = hours * rate

bonus = (hours // 40) * 50

total_pay = base_pay + bonus

is_premium = (total_pay > 2000) and (hours >= 40)

print("Name:", name)
print("Total Pay:", total_pay)
print("Premium Status:", is_premium)