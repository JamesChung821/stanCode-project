"""
File: rocket.py
Name: James Chung
---------------
This program plans to build up an rocket.
"""

# This number controls the size of the rocket.
SIZE = 3

def main():
    # Print("stanCode \nSC001", end="")
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    Create a rocket head
    """
    # Create /\ three times
    for h in range (SIZE): # h is from 0 to SIZE-1
        # Create space from 3 to 1
        for h1 in range (SIZE-h):
            print(" ", end="")
        for h2 in range (h+1):
            print("/", end="")
        for h3 in range (h+1):
            print("\\", end="")
        for h4 in range (SIZE-h):
            print(" ", end="")
        print("\n", end="")


def belt():
    """
    Create a rocket belt
    """
    print("+", end="")
    for b in range (SIZE):
        print("==", end="")
    print("+")


def upper():
    """
    Create a upper rocket body
    """
    for u in range (SIZE):
        print("|", end="")
        for u1 in range (SIZE-u-1):
            print(".", end="")
        for u2 in range (u+1):
            print("/", end="")
            print("\\", end="")
        for u1 in range (SIZE-u-1):
            print(".", end="")
        print("|")


def lower():
    """
    Create a lower rocket body
    """
    for l in range (SIZE):
        print("|", end="")
        for l1 in range (l):
            print(".", end="")
        for l2 in range (SIZE-l):
            print("\\", end="")
            print("/", end="")
        for l1 in range (l):
            print(".", end="")
        print("|")


######    DO NOT EDIT THE CODE BELOW THIS LINE    ######
if __name__ == '__main__':
    main()