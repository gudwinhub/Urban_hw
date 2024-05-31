class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __call__(self, width, height):
        return self.width * height

print(rect1(5, 5))