from functools import reduce
  
def oddTimes(input):
     print (reduce(lambda a, b: a ^ b, input))
  
# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 2, 3, 1, 3]
    oddTimes(input)