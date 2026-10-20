# 2 практическая python
# Begin6
a, b, c = float(input("Begin6. a: ")), float(input("b: ")), float(input("c: "))
print(f"V: {a*b*c:.2f} | S: {2*(a*b + b*c + a*c):.2f}\n")

# Begin7
R = float(input("Begin7. R: "))
print(f"L: {2*3.14*R:.2f} | S: {3.14*R**2:.2f}\n")

# Begin8
print(f"Begin8. Ср. арифм: {(float(input('a: ')) + float(input('b: '))) / 2:.2f}\n")

# Begin9
a, b = float(input("Begin9. a (>=0): ")), float(input("b (>=0): "))
print(f"Ср. геом: {math.sqrt(a * b):.2f}\n" if a >= 0 and b >= 0 else "Ошибка\n")

# Begin10
a, b = float(input("Begin10. a (!=0): ")), float(input("b (!=0): "))
if a and b: print(f"+: {a**2+b**2:.2f} | -: {a**2-b**2:.2f} | *: {a**2*b**2:.2f} | /: {a**2/b**2:.2f}\n")

# Begin11
a, b = float(input("Begin11. a (!=0): ")), float(input("b (!=0): "))
if a and b: print(f"+: {abs(a)+abs(b):.2f} | -: {abs(a)-abs(b):.2f} | *: {abs(a)*abs(b):.2f} | /: {abs(a)/abs(b):.2f}\n")

# Begin12
a, b = float(input("Begin12. Катет a: ")), float(input("Катет b: "))
hyp = math.sqrt(a**2 + b**2)
print(f"c: {hyp:.2f} | P: {a + b + hyp:.2f}\n")

# Begin13
R1, R2 = float(input("Begin13. R1: ")), float(input("R2 (<R1): "))
print(f"S1: {3.14*R1**2:.2f} | S2: {3.14*R2**2:.2f} | S3: {3.14*(R1**2 - R2**2):.2f}\n" if R1 > R2 else "Ошибка\n")

# Begin14
L = float(input("Begin14. L: "))
r = L / (2 * 3.14)
print(f"R: {r:.2f} | S: {3.14 * r**2:.2f}\n")

# Begin15
S = float(input("Begin15. S: "))
r = math.sqrt(S / 3.14)
print(f"D: {2*r:.2f} | L: {2*3.14*r:.2f}\n")

# Begin16
print(f"Begin16. Расстояние: {abs(float(input('x2: ')) - float(input('x1: '))):.2f}\n")

# Begin17
A, B, C = float(input("Begin17. A: ")), float(input("B: ")), float(input("C: "))
print(f"AC: {abs(C-A):.2f} | BC: {abs(C-B):.2f} | Сумма: {abs(C-A)+abs(C-B):.2f}\n")

# Begin18
A, B, C = float(input("Begin18. A: ")), float(input("B: ")), float(input("C (между): "))
print(f"Произведение AC*BC: {abs(C-A) * abs(C-B):.2f}\n")

# Begin19
x1, y1 = float(input("Begin19. x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
w, h = abs(x2 - x1), abs(y2 - y1)
print(f"P: {2*(w+h):.2f} | S: {w*h:.2f}\n")
