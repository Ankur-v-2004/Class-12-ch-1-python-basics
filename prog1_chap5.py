# Adding elements in a list
def main():
    L = []
    n = int(input("Total no of values in list: "))
    i = 1
    while i <= n:
        a = int(input("Enter element : "))
        if a%2 == 0:
            L.append(a)
            i = i+1
    print(L)
