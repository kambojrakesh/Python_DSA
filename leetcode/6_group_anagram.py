words = ["eat","tea","tan","ate","nat","bat"]
o = [["bat"],["nat","tan"],["ate","eat","tea"]]

# empty dictionary for anagrams together 
myDict = {} 
  
# traversal 
for val in words: 
      
    # sorts list
    key = ''.join(sorted(val)) 
    #print(key)
    if key in myDict.keys(): 
        myDict[key].append(val) 
    else: 
        myDict[key] = [] 
        myDict[key].append(val) 


print([*myDict.values()])