#Cesantías y prima
def Valor_cesantias(salario_mensual, dias_trabajados):
    cesantias = salario_mensual * dias_trabajados / 360
    #siempre se debe calcular el interes
    interes = cesantias * 0.12 * dias_trabajados / 360
    total_cesantias = cesantias + interes
    return total_cesantias

def Valor_prima(salario_mensual, dias_trabajados):
    prima = salario_mensual * dias_trabajados / 360
    total_prima = prima
    return total_prima


salario = float(input("Por favor ingrese salario"))
dias_trabajados = float(input("Por favor indiqueme los dias que trabajo"))
empleado1cesantia = Valor_cesantias(salario, dias_trabajados)
empleado1prima = Valor_prima(salario, dias_trabajados)

"""La especificación :.0f indica que no se deben imprimir decimales y que el número debe ser formateado como un número 
de punto flotante."""
print(f"las cesantias a pagar son,: {empleado1cesantia:.0f}")
print(f"la prima a pagar es de,: {empleado1prima:.0f}")