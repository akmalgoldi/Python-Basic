
#python default arguments
def greet(name, date, msg="Balikpapan"):
    """Fungsi ini menyapa 
    orang dengan pesan yang disediakan.
    
    Jika tidak ada pesan yang diberikan,
    maka pesan default akan digunakan.
    """
    print("Nama", name ,"Lahir pada tanggal", date , "di", msg)
greet("akmal", 2005)
greet("nabil", 2004, "Jakarta")
