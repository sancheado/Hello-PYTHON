# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\nEste es un String \n escapado"
print(my_scape_string)


# Formateo

name, surname, age = "Jose", "Sánchez Mateo", 35
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es {{(%s) [%s]}} y mi edad es _-[%s]-_" %(name,surname,age))
