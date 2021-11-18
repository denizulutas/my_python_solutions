def isprime(num):

  if num > 1:
    count = 0
    for i in range(2, num):
      if num% i == 0:
        count = 1
        break
  
  
  
  if count:                                               
    print("{} is not a prime number".format(num)) 
  else:
    print("{} is a prime number".format(num))

num1 =int(input("enter a num"))    
 
isprime(num1)   
