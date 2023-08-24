dia = input("Ingrese el día del parqueo: ")
horas = float(input("Ingrese las horas de parqueo: "))
minutos = int(input("Ingrese los minutos que se pasó: "))

if dia.lower() == "lunes" or dia.lower() == "martes" or dia.lower() == "miércoles":
    if minutos < 5:
        valor_pagar = horas * 2.00
    elif minutos >= 5 and minutos <= 60:
        valor_pagar = (horas + 1) * 2.00
    print(f"El valor a pagar por parquear el día {dia.lower()} con hora {horas} y minutos de {minutos} es de: {valor_pagar}")

elif dia.lower() == "jueves" or dia.lower() == "viernes":
    if minutos < 5:
        valor_pagar = horas * 2.50
    elif minutos >= 5 and minutos <= 60:
        valor_pagar = (horas + 1) * 2.50
    print(f"El valor a pagar por parquear el día {dia.lower()} con hora {horas} y minutos de {minutos} es de: {valor_pagar}")

elif dia.lower() == "sabado" or dia.lower() == "domingo":
    if minutos < 5:
        valor_pagar = horas * 3.00
    elif minutos >= 5 and minutos <= 60:
        valor_pagar = (horas + 1) * 3.00
    print(f"El valor a pagar por parquear el día {dia.lower()} con hora {horas} y minutos de {minutos} es de: {valor_pagar}")


