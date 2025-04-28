class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print("25°C in Fahrenheit is:", TemperatureConverter.celsius_to_fahrenheit(25))
