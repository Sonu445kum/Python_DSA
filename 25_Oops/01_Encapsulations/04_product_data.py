class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Getter
    def get_price(self):
        return self.__price

    # Setter with validation
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

# Usage
p = Product("Laptop", 50000)
print(p.get_price())   # 50000
p.set_price(55000)     
print(p.get_price())   # 55000
p.set_price(-100)      # Invalid
