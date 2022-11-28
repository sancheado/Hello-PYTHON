# Variables
my_string_variable = "Las variables me las saco de los cojones amigo!."
print("my_string_variable: " , my_string_variable)

my_int_variable = 5
print("my_int_variable: " , my_int_variable)


my_int_to_str_variable = str(my_int_variable)
print("my_int_to_str_variable: " , my_int_to_str_variable)

print("type(my_int_to_str_variable): " , type(my_int_to_str_variable))

my_bool_variable = False
print("my_bool_variable: " , my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable , my_int_to_str_variable, my_bool_variable)
# print(type(print(my_string_variable , my_int_to_str_variable, my_bool_variable)))
print("Este es el valor de: ", my_bool_variable)

# Algunas funciones del sistema
print("len(my_string_variable): " , len(my_string_variable))

# Variables de una sola línea !Cuidado con abusar de esta sintaxis¡
name, surname, alias, age = "Jose", "Sánchez Mateo", "Sancheado", 35
print("Me llamo:(", name, surname, "), mi edad es[", age, "] y mi alias es: -", alias , "- .")

# Inputs
# name = input('Cuál es tu nombre? ')
# age = input('Cuántos años tienes? ')


# Cambiamos su tipo
name = 35
age = "Jose"
print(name)
print(age)

# Forzamos el tipo
address: str = "Mi dirección"
address = 32
print(type(address))

'''
Este también es un 
comentario 
en varias lineas
'''