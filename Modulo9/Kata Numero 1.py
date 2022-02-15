def generate_report(main_tank, external_tank, hydrogen_tank):
    total_average = (main_tank + external_tank + hydrogen_tank) / 3
    return f"""Fuel Report:
    Total Average: {total_average}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """
# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(generate_report(80, 70, 85))
# Función promedio 
def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

# Test the averaging function with a list of integers:
average([80, 85, 81]) 
# Actualiza la función
def generate_report(main_tank, external_tank, hydrogen_tank):
    return f"""Fuel Report:
    Total Average: {average([main_tank, external_tank, hydrogen_tank])}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """

# Call the updated function again with different values
print(generate_report(88, 76, 70))
