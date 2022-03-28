class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(carnelian.color)
print(granny_smith.flavor)


class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound}! I'm {name}! {sound}!".format(name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink"


hamlet = Piglet("Hamlet")
hamlet.speak()


class Cow(Animal):
    sound = "Mooooo"


cow = Cow("Milky White")
cow.speak()


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


# Composition
# Using attributes and methods of one class when other is not direct child of it is Composition

class Repository:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def remove_package(self,package):
        del self.packages[package.name]

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += self.size
        return result



# Exmaples

class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)