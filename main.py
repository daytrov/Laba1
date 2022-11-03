import math
print("Введите коэффиценты квадратного уравнения:")
koef_A = int(input())
koef_B = int(input())
koef_C = int(input())
koren_x1 = 0
koren_x2 = 0
discrimiant = koef_B**2 - 4*koef_A*koef_C
if discrimiant > 0 :
    koren_x1 = -((koef_B+math.sqrt(discrimiant))/2*koef_A)
    koren_x2 = -((koef_B-math.sqrt(discrimiant))/2*koef_A)
    print("Корни квадратного уравнения: \n", "Первый корень = ", round(koren_x1), "\n", "Второй корень = ", round(koren_x2))
if discrimiant == 0 :
    koren_x1 = -(koef_B/(2*koef_A))
    print('Корни квадратного уравнения: \n', "Первый корень = ", round(koren_x1), "\n", "Второй корень = ", round(koren_x1))
if discrimiant < 0 :
    print('Корней квадратного уравнения не существует')