def z(n, c):
     if n == 0:
         return 0
     else:
       return z(n - 1, c) ** 2 + c
     
for n in range(10):
    print(f"z({n}) = {z(n, c=1)}")

def sequence(c):
     z = 0
     while True:
         yield z
         z = z ** 2 + c


for n, z in enumerate(sequence(c=1)):
     print(f"z({n}) = {z}")
     if n >= 9:
         break