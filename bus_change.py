'''
Create a python script to simulate a bus conductor collecting fare. The fare for each passenger
is fixed at 5 rupees. There are 5 passengers, and each passenger can pay an amount that is a
multiple of 5(up to 100). The conductor must provide change if required. The program should
output "True" if the conductor is able to give correct change to all passengers, and "False"
otherwise.
'''

passenger = []
passenger.append(int(input("Passenger 1: ")))
passenger.append(int(input("Passenger 2: ")))
passenger.append(int(input("Passenger 3: ")))
passenger.append(int(input("Passenger 4: ")))
passenger.append(int(input("Passenger 5: ")))
valid = [5,10,20,50,100]
for i in passenger:
    if i in valid:
        print()
    else:
        print(f"{i} is Invalid")
        break
if sum(passenger)>50:
    print("False")
elif passenger.count(10)>2:
    print("False")
else:
    print("True")