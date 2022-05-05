from math import sqrt

#Using map() function and lambda and count() function create a
# list consisted of the number of occurence of both letters: A and a.
def count_occurances():
    new_list =[]
    lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "aMontana", "Nevada"]
    count_of_A = 0
    count_of_a = 0
    for str in lst1:
        list1 = []
        list1[:0] = str
        count_of_A = count_of_A + list(map(lambda x: 1 if 'A' in x else 0, list1)).count(True)
        count_of_a = count_of_a + list(map(lambda x: 1 if 'a' in x else 0, list1)).count(True)
    new_list.extend(['A', count_of_A, 'a', count_of_a])
    return new_list

print("number of occurence of both letters: A and a: \n", count_occurances())

#Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))
x = int(input("Enter x Number: "))
root = lambda a, b, c, x: ((a*(x*x)) + (b*x) + c)
print(root( a, b, c, x))