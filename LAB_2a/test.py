# 1. Built-in constants
#========================================
constVar1 = True
print(constVar1)
constVar2 = None
print(constVar2)

print()

# 2. Python functions
#========================================
# first function - len()
str = 'Didukh'
print('Count of letter in my surname is', len(str))

# second function - sorted()
numbers = [0, 1, 10, 1, 5, 3, 4, 11]
print('Reverse sorted elements:', sorted(numbers, reverse=True))

# third function - type()
print('Var "str" is', type(str))

print()

# 3. Loops and Branching
#========================================
for n in range(0, 30, 3):
    print(n, end = " ")
print()
    
for i in range(2, 10, 2):
    for j in range(4):
        val = i - j
        if val % 2 == 0:
            print('Even number', val)
        else:
            print('Odd number', val)
            
print()
    
# 4. Exception
#========================================
try:
	print('2 + "str" = ???"')
	testVal = 2 + 'str'
except TypeError as exc:
	print(exc)
else:
    print('All right!')
finally:
	print("Oh No!")

print()

# 5. Context Manager - with
#========================================
with open("text_file.txt", 'w') as file:
	file.write('Lorem Ipsum')

# 6. Lambda
#========================================
def testFunc(n):
    return lambda x: x + n

func = testFunc(1)

print(func(3))