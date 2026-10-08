
m1 = int(input(" marks of subject 1: "))
m2 = int(input(" marks of subject 2: "))
m3 = int(input(" marks of subject 3: "))
m4 = int(input(" marks of subject 4: "))
m5 = int(input(" marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")
print("Percentage >= 75%:", percentage >= 75)
