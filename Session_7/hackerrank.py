

def area(length: int, width: int) -> int:
    return length * width


# when running imports, it executes the code in the file. 
# To avoid this, we use the following if statement:
# it checks if the file is being run directly or being imported
if __name__ == "__main__":
    x = area(3, 4)
    print(f"Area of rectangle is {x}")

    # defining variables as user input: 
    y = input()