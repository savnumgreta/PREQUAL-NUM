def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

def premier(m):
    if  m% 2 != 0:
        print("Le nombre doit être pair.")
        return

    for b in range(2, m//2):
        if est_premier(b):
          a =  m - b
          if est_premier(a):
            print(m, "=", a, "+", b)
    return a, b

m = 1136
a, b = premier(m)