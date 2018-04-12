def solveMeFirst(a,b):
   # Hint: Type return a+b below 
    if isinstance(a, int) and isinstance(b, int):
        sum = a+b
        return sum
    else:
        print ("{}, {} must be integers".format(a,b))
  

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)