print('Temperature Conversion Program')
def calculate_farenheit(celciusValue):
    farenheitValue = celciusValue * 9 / 5 + 32
    return farenheitValue


def calculate_kelvin(celciusValue):
    kelvinValue = celciusValue + 273
    return kelvinValue


celciusValue = float(input('Enter temperature in celcius: '))
farenheitValue = calculate_farenheit(celciusValue)
kelvinValue = calculate_kelvin(celciusValue)

print('Celcius value: ',celciusValue)
print('Farenheit value: ', farenheitValue)
print('Kelvin value: ', kelvinValue)