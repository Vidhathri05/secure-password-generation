import random

def passwordGen(length,use_capital=True,use_symbols = True,use_numbers = True):
    capital = ("".join(chr(i) for i in range(65,91)))
    symbols = ("".join(chr(i) for i in range(32,127) if not chr(i).isalnum()))
    numbers = ("".join(chr(i) for i in range(48,58)))
    lowercase = "".join(chr(i) for i in range(97, 123)) 
    types = 1
    all_chars = lowercase
    final = [random.choice(lowercase)] 
    if use_capital:
        all_chars+=capital
        final.append(random.choice(capital))
        types += 1
    if use_symbols:
        all_chars += symbols
        final.append(random.choice(symbols))
        types += 1
    if use_numbers:
        all_chars+= numbers
        final.append(random.choice(numbers))
        types += 1
    while len(final) < length:
        final.append(random.choice(all_chars))
    
    random.shuffle(final)
    password = "".join(final)
    return password,types

def types_evaluate(password, types):
    length = len(password)
    if length < 8 or types < 2:
        return "Weak"
    elif length >= 8 and types >= 2 and (length < 12 or types < 4):
        return "Medium"
    elif length >= 12 and types >= 4:
        return "Strong"
    else:
        return "Undefined"


length = int(input("enter password length"))
while length < 6:
    print("minimum length should be 6")
    length = int(input("Enter password length"))
capital = input("Include Capital letters ?(y/n)").lower() == 'y'
symbols = input("Include symbols ? (y/n)").lower() == 'y'
numbers= input("Include Numbers ? (y/n)").lower() == 'y'

if (capital or symbols or numbers):
    generated_password,types = passwordGen(length,capital,symbols,numbers)
    strength = types_evaluate(generated_password,types)
    print("Generated secure password is:",generated_password)
    print("password strength :",strength)
else:
    print("capital or symbols or numbers any one must be included")
    
    
