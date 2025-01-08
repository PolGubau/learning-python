def print_address(**kwargs)->None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Main St", 
              city="New York", 
              state="NY", 
              zip="10001")