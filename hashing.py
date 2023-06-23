
from fractions import Fraction
from random import randint

class PerfectHash:
    def __init__(self, keys):
        self.size = len(keys)  # Розмір хеш-таблиці
        self.table = [None] * self.size  # Ініціалізація хеш-таблиці
        self.a = None  # Коефіцієнти вторинної хеш-функції
        self.b = None  # Коефіцієнти вторинної хеш-функції
        self.generate_hash(keys)  # Генерація ідеальної хеш-функції

    def generate_hash(self, keys):
        # Крок 1: Розрахунок основного хешу для кожного ключа
        primary_hash = [self.hash_fraction(key) for key in keys]

        # Крок 2: Перевірка колізій та визначення розмірів другорядних таблиць
        secondary_sizes = [0] * self.size
        secondary_tables = [[] for _ in range(self.size)]
        for i, key in enumerate(keys):
            index = primary_hash[i] % self.size
            secondary_tables[index].append(key)
            secondary_sizes[index] += 1

        # Крок 3: Генерація вторинних хеш-функцій
        self.a = [[None] * size for size in secondary_sizes]
        self.b = [[None] * size for size in secondary_sizes]
        for i in range(self.size):
            if secondary_sizes[i] > 0:
                self.a[i] = [randint(1, 100) for _ in range(secondary_sizes[i])]
                self.b[i] = [randint(1, 100) for _ in range(secondary_sizes[i])]

        # Крок 4: Призначення ключів до хеш-таблиці з використанням ідеальної хеш-функції
        for i in range(self.size):
            if secondary_sizes[i] > 0:
                self.table[i] = [None for _ in range(secondary_sizes[i])]
                for j, key in enumerate(secondary_tables[i]):
                    index = (self.a[i][j] * primary_hash[i] + self.b[i][j]) % secondary_sizes[i]
                    self.table[i][index] = key

    def get(self, fraction):
        index = self.hash_fraction(fraction) % self.size
        if self.table[index] is not None:
            for j, key in enumerate(self.table[index]):
                if key == fraction:
                    return self.table[index][j]
        return None

    @staticmethod
    def hash_fraction(fraction):
        # Хешування раціонального числа
        numerator_hash = hash(fraction.numerator)
        denominator_hash = hash(fraction.denominator)
        hash_value = numerator_hash ^ denominator_hash
        print("Хеш для {}: {}".format(fraction, hash_value))
        return hash_value


keys = [Fraction(1, 2), Fraction(3, 4), Fraction(2, 3), Fraction(5, 7), Fraction(4, 9)]
hash_table = PerfectHash(keys)
print(hash_table.get(Fraction(2, 3)))
print(hash_table.get(Fraction(5, 7)))
print(hash_table.get(Fraction(4, 9)))
print(hash_table.get(Fraction(1, 2)))
