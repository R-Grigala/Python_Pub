def toFahrenheit(cel):
    return float((cel * 1.8) + 32)


celsius = float(input("Temperature value in degree Celsius: "))
print(celsius, "degree Celsius is equal", toFahrenheit(celsius), "Fahrenheit")

