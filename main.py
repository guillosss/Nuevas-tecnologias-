def averageStudent():
    average = 0
    for j in range(1,5):
        average = average + float(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average

def es_Int(variable):
    try:
        int(variable)
        return True
    except:
        return False

numAlumnos = 0
numMaterias = 0
students = []
materias = []
countWomen = 0
countMen = 0
countNotBinary = 0
averageTelecomunications = 0
averageSoftware = 0
countStudents = 0
averageAge = 0
countWomen = 0
countMen = 0
menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri) ")
if menu == "admi":
    numMaterias = input("Ingrese número de materias ")
    while True:
        if es_Int(numMaterias) == False or int(numMaterias) > 0:
            break
        else: 
            numMaterias = input("Ingrese número de materias ")
    numMaterias = int(numMaterias)
    numAlumnos = input("Ingrese número de alumnos ")
    while True:
        if es_Int(numAlumnos) == False or int(numAlumnos) > 0:
            break
        else:
            numAlumnos = input("Ingrese número de alumnos ")
    numAlumnos = int(numAlumnos)
    for nMat in range(numMaterias):
        nombreMateria = input("Ingrese el nombre de la " + str(nMat + 1) + " materia ")
        materias.append({"name": nombreMateria, "nota": 0})
    
    for i in range(numAlumnos):
        name = input("Ingrese nombre ")
        #print(materias)
        sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario) ")
        if sex == "m" or sex == "M":
            countWomen+=1
        elif sex == "h" or sex == "H":
            countMen+=1
        elif sex == "nb" or sex=="NB":
            countNotBinary+=1
        students.append({"name": name, "average": 0, "sexo": sex, "materias": []})
        for cMat in range(0,len(materias)):
            notaMateria = float(input("Ingrese la nota de la materia " + str(materias[cMat]["name"] + " ")))
            students[i]["materias"].append({"name": materias[cMat]["name"], "nota": notaMateria})

#medio por estudiante
    sumaMateriasM = 0
    sumaMateriasH = 0
    sumaMateriasNb = 0
    for al in range(numAlumnos):
        sumaMaterias = 0
        average = 0
        for alMat in range(numMaterias):
            sumaMaterias = sumaMaterias + students[al]["materias"][alMat]["nota"]
        average = sumaMaterias / numMaterias
        students[al]["average"] = average
        print("El promedio del estudiante " + str(students[al]["name"]) + " es de " + str(average))
        if students[al]["sexo"] == "m" or students[al]["sexo"] == "M":
            sumaMateriasM = sumaMateriasM + average
        elif students[al]["sexo"] == "h" or students[al]["sexo"] == "H":
            sumaMateriasH = sumaMateriasH + average
        elif students[al]["sexo"] == "nb" or students[al]["sexo"]=="NB":
            sumaMateriasNb = sumaMateriasNb + average
    print("El número de los estudiantes femeninos es " + str(countWomen))
    if countWomen > 0:
        print("El promedio de los estudiantes femeninos es " + str(sumaMateriasM / countWomen))
    print("El número de los estudiantes masculinos es " + str(countMen))
    if countMen > 0:
        print("El promedio de las estudiantes masculinos es " + str(sumaMateriasH / countMen))
    print("El número de los estudiantes no binarios es " + str(countNotBinary))
    if countNotBinary > 0:
        print("El promedio de los estudiantes NO Binarios es " + str(sumaMateriasNb / countNotBinary))
    

#medio por sexo estudiante
    for al in range(numAlumnos):
        sumaMateriasM = 0
        sumaMateriasH = 0
        sumaMateriasNb = 0
        for alMat in range(numMaterias):
            if students[al]["sexo"] == "m" or students[al]["sexo"] == "M":
                sumaMateriasM = sumaMateriasM + students[al]["materias"][alMat]["nota"]
            elif students[al]["sexo"] == "h" or students[al]["sexo"] == "H":
                sumaMateriasH = sumaMateriasH + students[al]["materias"][alMat]["nota"]
            elif students[al]["sexo"] == "nb" or students[al]["sexo"]=="NB":
                sumaMateriasNb = sumaMateriasNb + students[al]["materias"][alMat]["nota"]
    
#medio por estudiante
    for mat in range(numMaterias):
        sumaMaterias = 0
        for alMat in range(numAlumnos):
            sumaMaterias = sumaMaterias + students[alMat]["materias"][mat]["nota"]
        print("El promedio de la materia " + str(students[alMat]["materias"][mat]["name"]) + " es de " + str(sumaMaterias/numAlumnos))   