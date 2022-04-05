import numpy as np
import random
from Arbol import Arbol

import networkx as nx
import matplotlib.pyplot as plt


#Matriz de Total Caballos
Total = np.zeros((5, 5))
dimension = Total.shape
for x in range(dimension[0]):
    for y in range (dimension[1]):
        Total[x, y] = random.randint(0,99)
        
print ("Listado de participantes:" )
print (Total,'\n')
        
#Primeras 5 Carreras
print ("Listado de 5 primeras carreras:" )
for x in range(5):
  print(" Carrera ", x + 1, Total[x])


#Resultados primeras 5 carreras

print("\nResultados de menor a mayor: ")
for x in range(5):
  Total[x].sort() 
  print(" Carrera ", x + 1, Total[x]) 
  

#Carrera 6
print("\nCarrera 6 entre los mas rapidos:")
primeros= np.array([Total[0,4],Total[1,4],Total[2,4],Total[3,4],Total[4,4]])
print(primeros)

#Acomodo Final
print("\nAcomodo despues de carrera 6:")
final = Total[np.argsort(Total[:, 4])]
for x in range(5):
  print(final[x]) 

#Carrera 7
print("\nCarrera 7 por el segundo lugar:")
carrera7 = np.array([final[2, 4],final[3, 4],final[3, 3],final[4, 3],final[4, 2]])
print(carrera7)
carrera7.sort()

#Resultados
print("\nResultados:")
print("Primer lugar:", int(final[4,4]), "pts")
print("Segundo lugar:", int(carrera7[4]), "pts")

print("\nLista FINAL")
listafinal = np.concatenate(final)
listafinal.sort()
print(listafinal)

arbol= Arbol(int(Total[0, 0]), "Caballo  1")
arbol.agregar(int(Total[0, 1]),"Caballo  2")
arbol.agregar(int(Total[0, 2]),"Caballo  3")
arbol.agregar(int(Total[0, 3]),"Caballo  4")
arbol.agregar(int(Total[0, 4]),"Caballo  5")
arbol.agregar(int(Total[1, 0]),"Caballo  6")
arbol.agregar(int(Total[1, 1]),"Caballo  7")
arbol.agregar(int(Total[1, 2]),"Caballo  8")
arbol.agregar(int(Total[1, 3]),"Caballo  9")
arbol.agregar(int(Total[1, 4]),"Caballo 10")
arbol.agregar(int(Total[2, 0]),"Caballo 11")
arbol.agregar(int(Total[2, 1]),"Caballo 12")
arbol.agregar(int(Total[2, 2]),"Caballo 13")
arbol.agregar(int(Total[2, 3]),"Caballo 14")
arbol.agregar(int(Total[2, 4]),"Caballo 15")
arbol.agregar(int(Total[3, 0]),"Caballo 16")
arbol.agregar(int(Total[3, 1]),"Caballo 17")
arbol.agregar(int(Total[3, 2]),"Caballo 18")
arbol.agregar(int(Total[3, 3]),"Caballo 19")
arbol.agregar(int(Total[3, 4]),"Caballo 20")
arbol.agregar(int(Total[4, 0]),"Caballo 21")
arbol.agregar(int(Total[4, 1]),"Caballo 22")
arbol.agregar(int(Total[4, 2]),"Caballo 23")
arbol.agregar(int(Total[4, 3]),"Caballo 24")
arbol.agregar(int(Total[4, 4]),"Caballo 25")

arbol.lista()

Caballos = ["" for x in range(25)]

for x in range(25):
  Dato = arbol.buscar(listafinal[x])
  Caballos[x] = Dato.nombre
# print(Caballos[x])

#def CalcDis(Dup1, Dup2):
 #   return sqrt(pow((Dup1.x - Dup2.x), 2) + pow((Dup1.y - Dup2.y), 2))


Grafo = nx.Graph()
vertices_G = [Caballos[24], Caballos[23], Caballos[22], Caballos[21], Caballos[20],Caballos[19], Caballos[18], 
              Caballos[17], Caballos[16], Caballos[15], Caballos[14], Caballos[13], Caballos[12], Caballos[11], 
              Caballos[10], Caballos[9], Caballos[8], Caballos[7], Caballos[6], Caballos[5],Caballos[4],
              Caballos[3], Caballos[2], Caballos[1], Caballos[0]]

Grafo.add_nodes_from(vertices_G)

aristas_G = [(Caballos[24], Caballos[23]), (Caballos[23], Caballos[22]), (Caballos[22], Caballos[21]), (Caballos[21], Caballos[20]),
             (Caballos[20], Caballos[19]), (Caballos[19], Caballos[18]), (Caballos[18], Caballos[17]), (Caballos[17], Caballos[16]),
             (Caballos[16], Caballos[15]), (Caballos[15], Caballos[14]), (Caballos[14], Caballos[13]), (Caballos[13], Caballos[12]),
             (Caballos[12], Caballos[11]), (Caballos[11], Caballos[10]), (Caballos[10], Caballos[9]), (Caballos[9], Caballos[8]), 
             (Caballos[8], Caballos[7]), (Caballos[7], Caballos[6]), (Caballos[6], Caballos[5]), (Caballos[5], Caballos[4]),
             (Caballos[4], Caballos[3]), (Caballos[3], Caballos[2]), (Caballos[2], Caballos[1]), (Caballos[1], Caballos[0])]

Grafo.add_edges_from(aristas_G)

ubica = {Caballos[24]: (1, 17), Caballos[23]: (5, 17), Caballos[22]: (9, 17), Caballos[21]: (13, 17), Caballos[20]: (17, 17),
         Caballos[19]: (17, 13), Caballos[18]: (17, 9), Caballos[17]: (17, 5), Caballos[16]: (17, 1), Caballos[15]: (13, 1), 
         Caballos[14]: (9, 1), Caballos[13]: (5, 1), Caballos[12]: (1, 1), Caballos[11]: (1, 5), Caballos[10]: (1, 9),
         Caballos[9]: (1, 13), Caballos[8]: (5, 13), Caballos[7]: (9, 13), Caballos[6]: (13, 13), Caballos[5]: (13, 9),
         Caballos[4]: (13, 5), Caballos[3]: (9, 5), Caballos[2]: (5, 5), Caballos[1]: (5, 9), Caballos[0]: (9, 9)}



class Tupla:
    def _init_(self, x, y):
        self.x = x
        self.y = y

puntoA = Tupla()
puntoA.x = ubica[Caballos[24]][0]
puntoA.y = ubica[Caballos[24]][1]
puntoB = Tupla()
puntoB.x = ubica[Caballos[23]][0]
puntoB.y = ubica[Caballos[23]][1]
puntoC = Tupla()
puntoC.x = ubica[Caballos[22]][0]
puntoC.y = ubica[Caballos[22]][1]
puntoD = Tupla()
puntoD.x = ubica[Caballos[21]][0]
puntoD.y = ubica[Caballos[21]][1]
puntoE = Tupla()
puntoE.x = ubica[Caballos[20]][0]
puntoE.y = ubica[Caballos[20]][1]
puntoF = Tupla()
puntoF.x = ubica[Caballos[19]][0]
puntoF.y = ubica[Caballos[19]][1]
puntoG = Tupla()
puntoG.x = ubica[Caballos[18]][0]
puntoG.y = ubica[Caballos[18]][1]
puntoH = Tupla()
puntoH.x = ubica[Caballos[17]][0]
puntoH.y = ubica[Caballos[17]][1]
puntoI = Tupla()
puntoI.x = ubica[Caballos[16]][0]
puntoI.y = ubica[Caballos[16]][1]
puntoJ = Tupla()
puntoJ.x = ubica[Caballos[15]][0]
puntoJ.y = ubica[Caballos[15]][1]
puntoK = Tupla()
puntoK.x = ubica[Caballos[14]][0]
puntoK.y = ubica[Caballos[14]][1]
puntoL = Tupla()
puntoL.x = ubica[Caballos[13]][0]
puntoL.y = ubica[Caballos[13]][1]
puntoM = Tupla()
puntoM.x = ubica[Caballos[12]][0]
puntoM.y = ubica[Caballos[12]][1]
puntoN = Tupla()
puntoN.x = ubica[Caballos[11]][0]
puntoN.y = ubica[Caballos[11]][1]
puntoO = Tupla()
puntoO.x = ubica[Caballos[10]][0]
puntoO.y = ubica[Caballos[10]][1]
puntoP = Tupla()
puntoP.x = ubica[Caballos[9]][0]
puntoP.y = ubica[Caballos[9]][1]
puntoQ = Tupla()
puntoQ.x = ubica[Caballos[8]][0]
puntoQ.y = ubica[Caballos[8]][1]
puntoR = Tupla()
puntoR.x = ubica[Caballos[7]][0]
puntoR.y = ubica[Caballos[7]][1]
puntoS = Tupla()
puntoS.x = ubica[Caballos[6]][0]
puntoS.y = ubica[Caballos[6]][1]
puntoT = Tupla()
puntoT.x = ubica[Caballos[5]][0]
puntoT.y = ubica[Caballos[5]][1]
puntoU = Tupla()
puntoU.x = ubica[Caballos[4]][0]
puntoU.y = ubica[Caballos[4]][1]
puntoV = Tupla()
puntoV.x = ubica[Caballos[3]][0]
puntoV.y = ubica[Caballos[3]][1]
puntoY = Tupla()
puntoY.x = ubica[Caballos[2]][0]
puntoY.y = ubica[Caballos[2]][1]
puntoX = Tupla()
puntoX.x = ubica[Caballos[1]][0]
puntoX.y = ubica[Caballos[1]][1]
puntoZ = Tupla()
puntoZ.x = ubica[Caballos[0]][0]
puntoZ.y = ubica[Caballos[0]][1]


Puntos = {Caballos[24]: puntoA, Caballos[23]: puntoB, Caballos[22]: puntoC, Caballos[21]: puntoD, Caballos[20]: puntoE, 
          Caballos[19]: puntoF, Caballos[18]: puntoG, Caballos[17]: puntoH, Caballos[16]: puntoI, Caballos[15]: puntoJ, 
          Caballos[14]: puntoK, Caballos[13]: puntoL, Caballos[12]: puntoM, Caballos[11]: puntoN, Caballos[10]: puntoO, 
          Caballos[9]: puntoP, Caballos[8]: puntoQ, Caballos[7]: puntoR, Caballos[6]: puntoS, Caballos[5]: puntoT, 
          Caballos[4]: puntoU, Caballos[3]: puntoV, Caballos[2]: puntoY, Caballos[1]: puntoX, Caballos[0]: puntoZ}

cont: int = 0
'''for i in aristas_G:
    Pa = Puntos[aristas_G[cont][0]]
    Pb = Puntos[aristas_G[cont][1]]
    G.edges[i]['distancia'] = CalcDis(Pa, Pb)*100
    print('La distancia entre ', aristas_G[cont], G.edges[i],'[METROS]')
    cont = cont + 1'''
    
nx.draw(Grafo, pos=ubica, node_color='red', with_labels=True)
plt.show()