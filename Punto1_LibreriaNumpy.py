import numpy as np


Candidatos = 30
EstudiantesVotantes = 5000

votos = np.random.randint(0, Candidatos,EstudiantesVotantes)   # np.random.randint(Valor mas bajo, Valor mas alto, Cantidad de números aleatorios)
                                                                # 5000 numeros aleatorios entre 0 y 30

Conteo = np.bincount(votos, minlength=Candidatos) #Permite contar votos (Es la variable o matriz que contiene los votos, indica la cantidad de candidatos al array )
                                                           
orden_candidatos = np.argsort(-Conteo)   # np.argsort(array) Me permite ordenar los indices del array de menor a mayor,  np.argsort(-array) lo ordena de mayor a menor

# Imprimir resultados
print("Candidatos de mayor a menor de acuerdo a su cantidad de votos:")
for i, candidato in enumerate(orden_candidatos):                                #enumerate(variabledelarray) permite recorrer el array 
    print(f"Posición {i+1}: {Conteo[candidato]} votos Candidato {candidato+1} ")  #Conteo[candidato] se accede al arry conteo para obtener los votos del canditato

#JOHAN FRANCISCO LÓPEZ JAIMES