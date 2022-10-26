


amountRequired = 150  # <---can be changed to desired user input.
amountReturned = 0
counter_25 = 0
counter_10 = 0
counter_5 = 0
counter_1 = 0

while amountRequired >= 25:
        amountRequired -= 25
        counter_25 += 1

while amountRequired >= 10:
        amountRequired -= 10
        counter_10 += 1

while amountRequired >= 5:
        amountRequired -= 5
        counter_5 += 1

while amountRequired >= 1:
        amountRequired -= 1
        counter_1 += 1

print("____________________________________")
print("Amount of times the Racks have been used:")
print("25 Rack:",counter_25)
print("10 Rack:",counter_10)
print("5 Rack:",counter_5)
print("1 Rack:",counter_1)
