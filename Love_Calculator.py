print("Welcome to Love Calculator!! Here we predict your destiny with our love or crush")
your_name = input("What is your name? ")
lover_name = input("What is your lover's name? ")
your_name = your_name.lower()
lover_name = lover_name.lower()
c = your_name.count('t') + lover_name.count('t')

c = c+ your_name.count('r') + lover_name.count('r')
c = c+ your_name.count('u') + lover_name.count('u')
c = c+ your_name.count('e') + lover_name.count('e')
c2 = your_name.count('l') + lover_name.count('l')
c2 = c2 + your_name.count('o') + lover_name.count('o')
c2 = c2 + your_name.count('v') + lover_name.count('v')
c2 = c2 + your_name.count('e') + lover_name.count('e')

percentage = str(c)+str(c2)
print(percentage)







