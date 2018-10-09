# Hello World program in Python

'''    
class Person:
  __name = None
  def __init__(self, name, age):
    self.__name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.__name)

p1 = Person("John", 36)
p1.myfunc()
print(Person.__dict__)
'''


"""
def printIntersection(a1, a2):
    i1=0
    j1=0
    i2=len(a1)
    j2=len(a2)
    while ( i1<i2 and j1<j2):
        if (a1[i1] < a2[j1]):
            i1+=1
        elif (a1[i1] > a2[j1]):
            j1+=1
        else:
            print a1[i1]
            i1=i1+1
            j1=j1+1
            


printIntersection([0,1,2,3], [2,3,4])
"""
"""
def calcFib(n):
    dict = {}
    return calcFibHelper(n,dict)

def calcFibHelper(n, dict):
    if(n<0):
        dict[n] = 0
        return 0
    elif(n==0):
        dict[n] = 0
        return 0
    elif(n==1):
        dict[n] = 1
        return 1
        return dict[n]
    elif(n in dict):
        return dict[n]
    else:
        dict[n] = calcFibHelper(n-1, dict) + calcFibHelper(n-2, dict)
        return dict[n]
        

    
for i in range(301):
    print(str(i) + ": " + str(calcFib(i)))
"""
