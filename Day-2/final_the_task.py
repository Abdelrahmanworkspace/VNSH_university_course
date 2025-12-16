def parse_text(value):
    if value is None:
        return None 
    value = value.strip()
    if value == "":
        return None
    return value


def parse_int(value):
    if value is None:
        return None 
    value = value.strip()
    if value=="":
        return None 
    try:
        value =int(value)
        return value 
    except:
        return None 
        

from datetime import datetime 
def parse_date(value):
    if value is None:
        return None 
    value = value.strip()
    if value == "":
        return None
    try:
        date = datetime.strptime(value,'%d.%m.%Y')
        return date 
    except:
        return None

def required(value):
    if value is None :
        return False 
    try:
        return len(value)>=1
    except:
        return True 


def not_empty ( value):
    if value is None:
        return False
    value = value.strip()
    if value == "":
        return False
    try :
        return len(value)>=1
    except:
        return False

#it is the first function I forgot 
def min_length (n):
    def validator (value):
        if value is None:
            return True
        return len (value ) >= n
    return validator

#that is the second function I forgot 
def max_length (n):
    def validator ( value ):
        if value is None:
            return True 
        return len(value) <= n 
    return validator


#that is the third function I forgot 
def after_date ( n):
    def validator ( value ):
        if value is None :
            return True  
        return value > n
    return validator 


#that is the fourth function I forgot 
def before_date (n):
    def validator ( value ):
        if value is None :
            return True 
        return value < n 
    return validator 



def min_value (n):
    def validator(value):
        if value is None:
            return True
        else:
            return value>=n
    return validator 
    
check10 = min_value(10)

def max_value (n):
    def validator(value):
        if value is None:
            return True
        else:
            return value<=n
    return validator 
    
# check10 = min_value(10)

# check100 = max_value(100)
# min18 = min_value(18)
# # max65 = max_value(65)

# print(min_value(18)(15))   # False
# print(min18(20))   # True



# the fist version, it is work but it is stupid 
# def required(value):
#     if value is None or value =="":
#         return False 
#     if value == str:
#         value = value.strip()
#         if len(value)>=1:
#             return True 
#         else:
#             return False
#     else:
#         return True



def in_past(value):
    if value is None:
        return True
    
    if value < datetime.today():
        return True 
    return False

def in_future(value):
    if value is None:
        return True
    return value > datetime.today()

# print(in_future(datetime(2020,1,1)))

import re
def phone(value):
    if value is None:
        return True
    try:
        return bool(re.match(r'^\+7\d{10}$', value))
    except:
        return False

# print(phone("+71234")) # True
# phone("1234567890") # False
# phone("+712345") # False

def email(value):
    if value is None :
        return True
    try :
        return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value))
    except:
        return False

# print(email("wrong-email")) #True
# email("wrong-email")# False



def compose(*validators):

    def combined(value):

        for i in validators:
            if  i(value) == False:
                return False
        return True 
    return combined 



def single_validator(parse, validate):
    
    def validator(value):
        parse_in = parse(value)
        
        return validate(parse_in)
    return validator



def multi_validator(fields):
    def form_validator(input_data):
        results = {}
        for field_name, validator_func in fields.items():
            value = input_data.get(field_name) 
            is_valid = validator_func(value)
            results[field_name] = is_valid
        return results
    return form_validator