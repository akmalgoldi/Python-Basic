def greet(*name):
    """Fungsi ini menyapa orang dengan nama yang diberikan."""
    for name in name:
        print("Hello", name)

greet("akmal", "jaki", "Tono")
greet("akmal", "nabil", "fahmi", "budi")