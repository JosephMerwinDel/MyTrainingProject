def fibinocci_sequence(n):
    a = 1
    b= 1
    for i in range(n):
        yield a
        a,b = b, a+b

number = int(input("Enter input: "))
for nmber in fibinocci_sequence(number):
    print(nmber)

###
def executetwice(multiply):
	def inner(num1, num2):
		multiply(num1, num2)
		multiply(num1, num2)
	return inner

@executetwice
def multiply(num1, num2):
	print("Decorator: \n", num1 * num2)

number1 = int(input("Enter input 1: "))
number2 = int(input("Enter input 2: "))
multiply(number1,number2)



