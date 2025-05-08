def outer():
    x = "Local"
    
    def inner():
        nonlocal x
        x = "Nonlocal"
        print("inner: ", x)
    inner()
    print("outer: ", x)
    
outer()