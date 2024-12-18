print("enter a character")
input = input()

if  '0'<=input and input<='9' :
    print("\n","the character is a a number")
elif  input>= 'a' and input<= 'z':
    print("\n","the character entered is a lowecase alphabet")
elif  input>='A' and input<='Z':
    print("\n","the character entered is a uppercase alphabet")
else :
   print("\n","the entered character is neither an alphabet nor a number")
