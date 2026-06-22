def product_fib(_prod):
    f1 = 0
    f2 = 1
    
    while f1*f2 < _prod:   # checks if the product of numbers is less than give
        f1,f2 = f2,f2+f1   # goes to the next fibbonachi number
    
    is_match = (_prod == f1*f2)   # after exiting the loop, returns true if prod=f1*f2 if f1*f2 surpasses given prod it returns false
    
    return [f1,f2,is_match]
