from hashing import *
from b_plus_minus import *
from treap import *


print("----------------------------------------------\nRealization B+- tree: ")
tree = BPlusMinusTree(5)
tree.insert(5)
tree.insert(10)
tree.insert(3)
tree.insert(3.5)
tree.insert(-3.5)

print(tree.search(5))
print(tree.search(8))
print(tree.search(3.5))
print(tree.search(-3.5))
print("-----------------------------------------------")

print("----------------------------------------------\nRealization treap: ")
treap = Treap()
treap.insert(5)
treap.insert(10)
treap.insert(3)

print(treap.search(5))
print(treap.search(8))

treap.delete(5)
print(treap.search(5))
print("-----------------------------------------------")

print("----------------------------------------------\nRealization ideal hashing: ")
keys = [Fraction(1, 2), Fraction(3, 4), Fraction(2, 3), Fraction(5, 7), Fraction(4, 9)]
hash_table = PerfectHash(keys)
print(hash_table.get(Fraction(2, 3)))
print(hash_table.get(Fraction(5, 7)))
print(hash_table.get(Fraction(4, 9)))
print(hash_table.get(Fraction(1, 2)))
print("-----------------------------------------------")


