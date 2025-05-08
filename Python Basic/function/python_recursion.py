def factorial(x):
    """
    Fungsi rekursif untuk menemukan 
    factorial dari bilangan bulat
    """
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
num = 3
print("Faktorial dari", num, "adalah", factorial(num))