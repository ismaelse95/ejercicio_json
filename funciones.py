import json

with open("fichero.json") as file:
	fichero=json.load(file)

#Ejercicio 1
#def lista(variable):
variable=input()
for key,value in fichero.items():
	for value2 in value:
		#print(value2)
		if "Fecha_Publicacion" in value2:
			if value2["Fecha_Publicacion"] == variable:
					print(value2["Titulo"])