print("Welcome to the tip calculator!")
print("What was the total bill? $")
start_bill = float(input())
print("How much tip would you like to give? 10, 12, or 15? ")
tip_percent = int(input())
print("How many people to split the bill? ")
total_people = int(input())

total_bill = start_bill * (tip_percent / 100 + 1)
split_bill = total_bill / total_people
rounded_result = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${rounded_result}")
