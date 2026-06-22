def product_fib(_prod):
    f1 = 0
    f2 = 1
    
    while f1*f2 < _prod:
        f1,f2 = f2,f2+f1
    
    is_match = (_prod == f1*f2)
    
    return [f1,f2,is_match]
