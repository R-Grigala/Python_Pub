def toCelsius(far):
    return (far - 32) * 5/9


fahrenheit = float(input("Temperature value in degree Fahrenheit: "))
print(fahrenheit, "degree Fahrenheit is equal", toCelsius(fahrenheit), "Celsius ")

