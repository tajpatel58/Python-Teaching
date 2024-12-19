def list_length_checker(list1: list, list2: list):
    if len(list1) == len(list2):
        return True 
    else:
        return False
    

def is_number_Fizz_or_Buzz_or_FizzBuzz(my_number: int):
    if my_number % 3 == 0 and my_number % 5 == 0:
        print("FizzBuzz")
    elif my_number % 3 == 0:
        print("Fizz")
    elif my_number % 5 == 0:
        print("Buzz") 