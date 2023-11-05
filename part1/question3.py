class MagicalOven:
    def __init__(self):
        self.ingredients = []
        self.output = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.output = "ice cream"

    def boil(self):
        self.output = "soup"

    def wait(self):
        self.output = "mud"

    def get_output(self):
        return self.output

def make_oven():
    return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if "lead" in oven.ingredients and "mercury" in oven.ingredients and temperature >= 5000:
        oven.output = "gold"
    elif "water" in oven.ingredients and "air" in oven.ingredients and temperature <= -100:
        oven.output = "snow"
    elif "cheese" in oven.ingredients and "dough" in oven.ingredients and "tomato" in oven.ingredients and temperature >= 150:
        oven.output = "pizza"
    return oven.output

