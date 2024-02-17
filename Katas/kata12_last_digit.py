"""
Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a**b
Note that a and b may be very large

For example, the last decimal digit of 9**7  is 9 since  9**7 = 4782969
the last decimal digit of (2**200)2**200 wich has  over 10**92 decimal digits is 6, also place take 0**0 to be 1

Examples
last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
"""
def last_digit(a, b):
    if b == 0:
        return 1
    
    # Calcular el último dígito de a elevado a la potencia b
    a = a % 10  # Tomar solo el último dígito de a
    ciclos = b % 4 if b % 4 != 0 else 4  # Encontrar el ciclo repetitivo de los últimos dígitos
    resultado = (a ** ciclos) % 10  # Calcular el último dígito de a elevado a la potencia b
    
    return resultado

print(last_digit(2**200, 2**300))

# ---- Clever Solution 

# def last_digit(n1, n2):
#     return pow( n1, n2, 10 )

# ---- clever Solution 02
# def last_digit(n1, n2):
#     if n1%10 == 0:
#         x = 0
#     else:
#         x = ((n1%100)**(n2%100))%10
#     return x