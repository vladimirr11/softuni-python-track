number = float(input())
input_measurement_unit = (input())
output_measurement_unit = input()

if input_measurement_unit == 'mm' and output_measurement_unit == 'm':
    number = number / 1000
elif input_measurement_unit == 'm' and  output_measurement_unit == 'cm':
    number = number * 100
elif input_measurement_unit == 'cm' and output_measurement_unit == 'mm':
    number = number * 10
elif input_measurement_unit == 'mm' and output_measurement_unit == 'cm':
    number = number / 10
elif input_measurement_unit == 'cm' and output_measurement_unit == 'm':
    number = number / 100
elif input_measurement_unit == 'm' and output_measurement_unit == 'mm':
    number = number * 1000

print(f'{number:.3f}')