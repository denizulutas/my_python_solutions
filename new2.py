age = input("Are you a cigarette addict older than 75 years old? (please enter'yes' or 'no' for all questions )").strip().lower()
chronic = input("Do you have a severe chronic disease? ").strip().lower()
immune = input("Is your immune system too weak?").strip().lower()

if (age  or chronic or immune )=="yes":
  print("You are in risky group")
elif (age or chronic or immune)=="no":
  print("You are not in risky group")   
  

