# -*- coding: utf-8 -*-



#recursive 
def b_sort(ls, n = 0):
    
    for k, i in enumerate(ls[n:]):
      if k < len(ls)-1:
          fv = ls[k]
          sv = ls[k+1]
          if fv > sv:   
            ls[k] = sv
            ls[k+1] = fv
    
    n = n + 1
    if n <= len(ls) -1 :
        b_sort(ls, n)
        
    return ls

if __name__ == '__main__':
    numbers_list = [125,4,13,1,67,9,123,1,5]

    numbers_list = ["mona", "dhaval", "aamir", "tina", "chang"]
    ls = b_sort(numbers_list)
    print(ls)
    
#burute force    

def b_sort(ls):
    for o in range(0, len(ls)-1):
        for k, i in enumerate(ls[o:]):
          if k < len(ls)-1:
              fv = ls[k]
              sv = ls[k+1]
              if fv > sv:   
                ls[k] = sv
                ls[k+1] = fv
    return ls

if __name__ == '__main__':
    numbers_list = [125,4,13,1,67,9,123,1,5]


    ls = b_sort(numbers_list)
    print(ls)