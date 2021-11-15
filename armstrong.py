num =input("enter a number to check it is armstrong or not  :  ")
len_num =str(num)
sum_num = 0
if len_num.isnumeric() and int(len_num) > 0:

  for i in len_num:
    i = int(i)
    sum_num += i**len(len_num)
    i = i + 1
  
  if sum_num ==int(num):
    print("{} is a armstrong number".format(num))
  else:
     print("{} is not a armstrong number".format(num))

else:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values! ")
