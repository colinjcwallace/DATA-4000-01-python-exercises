x = int(input("What is x? "))
y = int(input("What is y? "))

if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x == y:
    print("x is equal to y")

# == is a conditional
# you get three outputs because you run three times. Need to use elif and else to get only one output
# you also dont need to ask all three questions. If not the first two then it must be equal

#----Reviesed Code----

x = int(input("What is x? "))
y = int(input("What is y? "))

if x > y:
    print("x is greater than y")    

elif x < y:
    print("x is less than y")

else:
    print("x is equal to y")
