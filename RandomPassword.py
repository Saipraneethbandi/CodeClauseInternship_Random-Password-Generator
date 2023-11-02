import random
import string


len=int(input("Enter the lenth of password:"))
 
lower_len=int(input("Enter no of lowercase charaters:"))
upper_len=int(input("Enter no of uppercase charaters:"))
digit_len=int(input("Enter no of digits:"))
symbol_len=int(input("Enter no of symbols:"))
 
password_len=lower_len+upper_len+digit_len+symbol_len
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
 
str=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=digit_len)+random.choices(symbol,k=symbol_len)

random.shuffle(str)
password="".join(str)

print("Generated password is:",password)