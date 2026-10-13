"""Deduplicar conservando el orden de aparición original. Es
decir, elimina las copias repetidas de una lista."""
ls=[1,2,3,4,5,6,7,8,9,9,9,9]

print(list(set(ls)))