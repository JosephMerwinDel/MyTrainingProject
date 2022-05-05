#Return all the duplicate values from list of arraylist
def get_duplicates_from_list_of_arraylist():
    arrlists = [[1, 2, 4], [5, 7, 2], [7, 4, 7]]
    dict ={}
    for list in arrlists:
        for i in range(len(list)):
            count = 0
            k = i + 1
            for j in range(k, len(list)):
                if list[i] == list[j]:
                    count = count + 1
            dict[list[i]] = count
    print(dict)

get_duplicates_from_list_of_arraylist()

#Merge two lists as shown below
def merge_two_lists(list1, list2):
    mergedList = []
    for str1 in list1:
        for str2 in list2:
            mergedList.append("{} {}".format(str1,str2))
    print("Output of Merge two lists: \n", mergedList)

list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
merge_two_lists(list1, list2)

#Map the dictionary in the following manner
def map_two_list_into_dict(keys, values):
    dict_new = dict(zip(keys, values))
    print("Map two list into one : \n ", dict_new)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
map_two_list_into_dict(keys, values)

#Merge following two Python dictionaries into one
def merge_two_dict():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print("Merge two dictionary: \n", dict1)

merge_two_dict()

#Rename key city to location in the following dictionary
def rename_key_dict(sampleDict):
    sampleDict["location"] = sampleDict.pop("city")
    print("Rename key city to location in dict: \n",sampleDict)

sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
rename_key_dict(sampleDict)

#Convert Dictionary to list
def convert_dictionary_to_list(dict):

    outputlist = []
    for key,value in dict.items():
        list = []
        list.append(key)
        for i in value:
            list.append(i)
        outputlist.append(list)
    print("Convert Dictionary to list: \n", outputlist)

dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
convert_dictionary_to_list(dict)