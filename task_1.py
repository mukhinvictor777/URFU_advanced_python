class Trio:

    def __init__(self, a):
        self.a = a

    def compare(self, b):
        if self.a == b:
            return "True"
        elif abs(self.a - b) / ((self.a + b) / 2) < 0.2:
            return "Maybe"
        else:
            return "False"

    def __eq__(self, other):
        if isinstance(other, Trio):
            return self.compare(other.a)
        return False


class Person(Trio):
    def __init__(self, a):
        super().__init__(a)

    def check(self, e):
        if e == 'Maybe':
            return self.maybe
        elif not e:
            return self.no
        elif e:
            return self.yes
        else:
            return "Некорректное высказывание"


class Soldier(Person):
    yes = "ДА"
    no = "НЕТ"
    maybe = "Это не солдат"


class Diplomat(Person):
    yes = "МОЖЕТ БЫТЬ"
    no = "Это не дипломат"
    maybe = "НЕТ"


class Woman(Person):
    yes = "Это не женщина, это солдат!"
    no = "МОЖЕТ БЫТЬ"
    maybe = "ДА"


a = Trio(10)
b = Trio(9)
c = Trio(10)
d = Trio(3)

print(a.a == b.a)
print(a.a == c.a)
print(a.a == d.a)
print(a.compare(b.a))
print(a.compare(c.a))
print(a.compare(d.a))
print(a == b)
print(a == c)
print(a == d)
print()
w = Woman(5)
dip = Diplomat(5)
sol = Soldier(5)
print(w.check(a == b))
print(dip.check(a.compare(b.a)))
print(sol.check(a.compare(b.a)))
