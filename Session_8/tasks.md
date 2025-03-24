# Python Exercise List 8:

### Task 1: Quadratic Equation Root Solver:
- Write a function that takes in 3 inputs, a, b and c which correspond to coefficients of a quadratic curve. 
- Then if the quadratic equation has atleast one root, the function returns the roots.
- Otherwise returns the string: "No Real Roots". 
- Note: you'll want to use the sqrt function from the "math" package. 

### Task 2: Prime Number Checker
- Write a function that takes in an integer and returns "Prime" if prime, and "Not Prime" if not prime. 
- Once you have done this, try google "isprime functions in Python". Try import the function and use it. 
- This shows you that code for common tasks are likely to have already been written by someone. 

### Task 3: List if Prime Numbers
- Write a function that takes in one integer (X). 
- Inside this function:
    - Create a list of the first X integers (use the Range function).
    - Return a dictionary where the keys are the first X integers and the values are whether the the key is prime or not. (NOTE: Use your prime number checker function)
    - Eg: {1: Not Prime, 2: Prime, 3: Prime, 4: Not Prime, .....}

### Task 4: Time
- Google what time.time() is? 
- Google how you can time how long it takes for code to run using time.time().
- Time how long it takes your code to create the dictionary in the task above for the first 1000 numbers. 
- Time how long it takes your code to create the dictionary in the task above if we use the built in isprime function that was imported? 