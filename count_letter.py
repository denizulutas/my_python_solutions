def count_letter():
  text=input("Enter a text:").strip()
  my_dict={}
  for i in set(text):
    my_dict[i]=text.count(i)
  print(my_dict)  

