import threading

# Definisi kelas menggunakan prinsip OOP
class Item:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    # Getter untuk name
    def get_name(self):
        return self.__name

    # Setter untuk name
    def set_name(self, name):
        self.__name = name

    # Getter untuk quantity
    def get_quantity(self):
        return self.__quantity

    # Setter untuk quantity
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")

    def __str__(self):
        return f'Item: {self.__name}, Quantity: {self.__quantity}'

class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def list_items(self):
        for item in self.__items:
            print(item)

    # Getter untuk items
    def get_items(self):
        return self.__items

# Fungsi dengan exception handling
def add_item_to_inventory(inventory, name, quantity):
    try:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        item = Item(name, quantity)
        inventory.add_item(item)
    except ValueError as e:
        print(f"Error: {e}")

# Contoh penggunaan multithreading
def process_inventory(inventory):
    print("Processing inventory in a separate thread...")
    for i in range(5):
        add_item_to_inventory(inventory, f"Item_{i}", i)

# Main program
if __name__ == "__main__":
    inventory = Inventory()
    try:
        threading.Thread(target=process_inventory, args=(inventory,)).start()
    except Exception as e:
        print(f"Threading error: {e}")

    # Tunggu hingga thread selesai
    threading.Event().wait(1)

    # List all items in inventory
    inventory.list_items()
