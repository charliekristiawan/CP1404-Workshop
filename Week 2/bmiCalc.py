print('Body-mass-index calculator, by Charlie')

weight = float(input('Please enter your weight in kgs: '))
height = float(input('Please enter your height in m: '))

BMI = weight / height**2

print('Therefore, your BMI value is: ', BMI)
print('Thank you!')
