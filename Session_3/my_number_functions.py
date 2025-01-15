def even_number_checker(my_number: int) -> bool:
    remainder = my_number % 2
    if remainder == 0:
        return True
    else:
        return False
    


def odd_number_checker(num: int) -> bool:
    remainder = num % 2 
    if remainder == 0:
        return False
    else:
        return True