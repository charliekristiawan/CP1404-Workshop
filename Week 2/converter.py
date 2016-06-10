print('Temperature Conversion program')

celciusValue = float(input('Enter the temperature today: '))
fahrenheitValue = celciusValue * 9 / 5 + 32
kelvinValue = celciusValue + 273

print('celcius value: ', celciusValue)
print('fahrenheit value: ', fahrenheitValue)
print('kelvin value: ', kelvinValue)