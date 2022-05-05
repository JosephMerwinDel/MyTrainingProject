from functools import reduce

def filters(number):
    if(number < 0):
        #print(abs(number))
        return abs(number)
    else:
        return 0

lst1 = [-1000, 500, -600, 700, 5000, -900]
result = filter(lambda x: x > 0 , list(map(filters, lst1)))
lst5 = list(result)
print("Output: \n", list(result))


print("Output: \n", reduce(lambda a, b: a*b, lst5))


lst1 = ['Netflix', 'Hulu', 'Sling', "Hbo"]
lst2 = [198, 166, 237, 125]
dictionary = dict(zip(lst1, lst2))
print("Dictionary Output: \n", dictionary)