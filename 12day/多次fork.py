import os

p = os.fork()

if p == 0:
    print("son")
else:
    print("father")

p = os.fork()

if p == 0:
    print("son1")
else:
    print("father")
