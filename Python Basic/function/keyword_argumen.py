def greet(name, msg):
    """Function to greet a person with a message."""
    print("Hello" ,name, msg)

# 2 keyword arguments
greet(name = "akmal", msg = "selamat datang")

# 2 keyword arguments (out of order)
greet(msg = "selamat datang", name = "akmal")

# 1 positional argument, 1 keyword argument
greet("akmal", msg = "selamat datang")

