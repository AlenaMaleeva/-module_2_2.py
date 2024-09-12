first = 2
second = 2
third = 2
print( first, second, third )
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second != third:
    print(0)
