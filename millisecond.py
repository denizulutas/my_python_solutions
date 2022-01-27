def watch():
  num = input('Enter milliseconds to convert:  ')


  if num.isalpha():
    if num == 'exit':
      return "Exiting the program... Good Bye"
    else:
      return "Not Valid Input !!!" 
  elif num.isdecimal:
    num = int(num)
    if num < 0:
      return "Not Valid Input !!!"
    elif num <1000 and num >0:
      return 'just {} millisecond/s'.format(num)
    elif num >= 1000:
      result = ''

      hour = num // 3600000
      hour1 = num % 3600000
      minute = hour1 // 60000
      minute1= hour1 % 60000
      second = minute1 //1000
      second1 =minute1 % 1000

      if hour > 0:
        result = result + str(hour) + ' hour/s ' 
      if minute >0:
        result = result + str(minute) + ' minute/s '
      if second > 0:
        result = result + str(second) + ' second/s ' 

      return result  

