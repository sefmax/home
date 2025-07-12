class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Item(name={self.name}, price={self.price}, description={self.description}, dimensions={self.dimensions})"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"User(name={self.name}, surname={self.surname}, phone={self.numberphone})"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt
        self.total += item.price * cnt

    def __str__(self):
        items_str = "\n".join([f"{item.name} x {cnt} = {item.price * cnt}" for item, cnt in self.products.items()])
        return f"Purchase by {self.user.name} {self.user.surname}:\n{items_str}\nTotal: {self.get_total()}"

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())