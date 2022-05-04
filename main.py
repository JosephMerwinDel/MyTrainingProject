'''Exercise_1 - create a class with name StringClass which should take string as an input from constructor.
It should have method which should return the length of the string and a method to convert string to list of characters.
This method will take an argument as string to convert'''
class StringClass:

    def __init__(self, str):
        self.str = str

    def get_length_of_string(self):
        return len(self.str)

    def convert_string_to_list(self, str):
        list1 =[]
        for chr in str:
            list1.append(chr)
        return list1

'''Exercise_2- Create class PairsPossible which should inherit from StringClass and 
should have a method for storing list of all possible pairs formed. It should also have a method to print list of 
every possible pair in same line but with space between them. Pairs should be in list.'''
class PairsPossible(StringClass):

    def __init__(self, strlist):
        self.strlist = strlist

    def pairs(self):
        possiblePairList =[]
        #print(len(self.strlist))
        for i in range(0, len(self.strlist)):
            for j in range(0, len(self.strlist)):
                if (i != j):
                    possiblePairList.append((self.strlist[i], self.strlist[j]))
        return possiblePairList

'''Exercise_3 - Create a class SearchCommonElements which should take up a string. 
Your task is to create a method to find common elements from string taken in StringClass and string taken in PairsPossible class and return the answer in list. 
Note- Please use dictionary logic to find common elements.'''
class SearchCommonElements:

    def __init__(self, str3):
        self.str3 = str3

    def common_elemets(self, stringValue):
        outputList = []
        for i in stringValue:
            if i in self.str3  and not i in outputList:
                outputList += i
        return outputList

'''Create a class EqualSumPairs to get the count of total number of pairs formed in class PairsPossible which has sum which is not equal to sum of other pairs. 
Print the output for SearchCommonElements and EqualSumPairs classes'''
class EqualSumPairs:


#Objects
stringValue = input("Enter String value: ")
strBaseObj = StringClass(stringValue)
print("The length of the given String is: \n",strBaseObj.get_length_of_string())

list2 = strBaseObj.convert_string_to_list(stringValue)
print("The converted string to list of characters is: \n",list2)

strchildObj = PairsPossible(list2)
print("Pairs of possible combination in the list \n", strchildObj.pairs())

strSearchCommonElements = SearchCommonElements(stringValue)
string_check = input("Enter String value to check with: ")
outputList = strSearchCommonElements.common_elemets(string_check)
print("Common elements from string taken in StringClass and string taken in PairsPossible class is \n", outputList)


