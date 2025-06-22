import enum
class dia_da_semana(enum.IntFlag):
    segunda = 1
    terca = 2
    quarta = 3
    quinta = 4
    sexta = 5
    sabado = 6
    domingo = 7

a = dia_da_semana.segunda
b = dia_da_semana.terca
c = dia_da_semana.quarta

print(a) # dia_da_semana.segunda
print(b) # dia_da_semana.terca
print(c) # dia_da_semana.quarta

#.name da o nome do enum
print(a.name) # dia_da_semana.segunda
print(b.name) # dia_da_semana.terca
print(c.name) # dia_da_semana.quarta

# O operador | faz a união de dois ou mais elementos
#O operador & faz a interseção, testando se um elemento está no conjunto: se o resultado for igual a zero, o elemento não está no conjunto
print(a | b) # dia_da_semana.segunda | dia_da_semana.terca
print(a & b) # dia_da_semana.segunda & dia_da_semana.terca