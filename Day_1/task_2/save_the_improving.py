file = open("text.txt","r")
lines=file.readlines()
import re
from decimal import Decimal

dictionary = {}

for i in lines :
    line = re.match(r'"(.+)" - (\d+): ([+-]\d+(?:\.\d+)?)',i)
    if line:
        name, account,amount = line.groups()
        account= int(account)
        amount = Decimal(amount)

        
        if name not in dictionary:
            dictionary[name]= {}

        if account not in dictionary[name]:
            dictionary[name][account]=0

        dictionary[name][account] =dictionary[name][account] +amount
        

# print(dictionary)
for name ,accounts in dictionary.items() :
    print( f'"{ name }" - {", ".join(f"{account}: {amount}" for account, amount in accounts.items())}')


file.close()