# Salario base x Días trabajados ÷ 360
def calculo_prima(salario_base, dias_trabajados, semestre):
    neto_prima = salario_base * dias_trabajados / semestre
    return neto_prima


def calculo_cesantias(salario_base: float, dias_trabajados: int, semestre: int) -> float:
    cesantias = salario_base * dias_trabajados / semestre
    return cesantias


# (cesantías acumuladas x días trabajados x 0.12 )/360
def intereses_cesantias(cesantias: float, dias_trabajados: int) -> float:
    intereses = (cesantias * dias_trabajados * 0.12) / 360
    return intereses


semestre = int(360)
salario = float(input("Ingrese por favor su salario"))
while salario < 1160000:
    print("No se puede realizar si su salario es menor ☻ a un SMLV")
    salario = float(input("Ingrese por favor su salario"))

dias_trabajados = float(input("Por favor ingrese los dias trabajados"))
while dias_trabajados < 1 or dias_trabajados > 180:
    print("El número de días trabajados debe estar entre 1 y 180.")
    dias_trabajados = float(input("Por favor ingrese los dias trabajados☺"))

prima_a_pagar = calculo_prima(salario, dias_trabajados, semestre)
cesantias_a_pagar = calculo_cesantias(salario, dias_trabajados, semestre)
interes_cesantias = intereses_cesantias(cesantias_a_pagar, dias_trabajados)
print(f"Valor total de la prima es de: {prima_a_pagar} por un total de, {dias_trabajados}")
print(f"Valor total de las cesantias es de: {cesantias_a_pagar} por un total de, {dias_trabajados}")
print(f"Valor total interes cesantias es de:{interes_cesantias}")
