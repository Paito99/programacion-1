#actividad 2.2.3
print("DETALLE ANUALIDAD COLEGIO ")

rut= input ("ingrese rut apoderado:")
nomAlum= input("ingrese el nombre del alumno:")
curso=input ("ingrese curso al cual el alumno debe matricularse:")
matricula =int(25000)
mensualidad= int (30000)
resultadoAnual=int(mensualidad*10)+ matricula 

print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR DE MATRICULA: {matricula}")
print(f"VALOR DE MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")


