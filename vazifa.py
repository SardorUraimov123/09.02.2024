class MyDataBase:
    def __init__(self):
        self.elements = []
        self.original_elements = []

    def __enter__(self):
        self.original_elements = self.elements.copy()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Xatolik: {exc_type}, {exc_value}")
            self.elements = self.original_elements.copy()

    def append(self, value):
        self.elements.append(value)

    def get_elements(self):
        return self.elements

with MyDataBase() as db:
    db.append(1)
    db.append(2)
    db.append(3)

print("Asl holat:", db.get_elements())
# 2-misol
class MyDataBase:
    def __init__(self):
        self.elements = []
        self.original_elements = []

    def append(self, value):
        self.elements.append(value)

    def commit(self):
        self.original_elements = self.elements.copy()

    def rollback(self):
        self.elements = self.original_elements.copy()

db = MyDataBase()

try:
    db.append(1)
    db.append(2)
    db.append(3)

    raise ValueError("Test xatolik")

except ValueError as e:
    print(f"Xatolik: {e}")
    db.rollback()

print("Asl holat:", db.original_elements)
