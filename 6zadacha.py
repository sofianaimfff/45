#Напишите программу, ĸоторая прогнозирует рост населения через ( n ) лет.
# Начальная численность населения ( P ) и
# процентный прирост ( r ) вводятся пользователем.

P = int(input("Начальная численность населения: "))
r = int(input("Процентный прирост численности: "))
n = 5 # кол-во лет

for i in range (1, n + 1):
    P = P + ( P * ( r / 100 ) )
print(P)