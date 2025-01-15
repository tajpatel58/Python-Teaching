

def string_reverser(string_to_reverse: str) -> str:
    list_string = list(string_to_reverse)
    list_string.reverse()
    joined_str = "".join(list_string)
    return joined_str
