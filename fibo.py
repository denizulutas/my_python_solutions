list1 =[]

for i in range(15):
  if i<=1:
    list1.append(1)
  else:
    list1.append(sum(list1[i-2:]))
    if 55 in list1:
      break

print(list1)
