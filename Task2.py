class TwoSum:  
    def __init__(self, lst, target):  
        self.lst = lst 
        self.target = target  
          
    def solution(self):  
        length = len(lst)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if lst[i]+lst[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)  
        return -1  
  
lst = []
n = int(input("Enter number of elements : "))
print("Enter element")
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)  

final_list = lst
print(final_list)

target = int(input("Enter The Target : "))  
obj = TwoSum(lst, target)  
print(obj.solution())  