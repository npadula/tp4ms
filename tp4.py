# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:46:46 2016

@author: npadula
"""

import numpy as np
import matplotlib.pyplot as plt

h = 0.025
n = int(1/h) + 1
cant = (n*n) -2 

S = np.zeros((cant,cant))
b = np.zeros(cant)



c = 0
for i in range(n): # Filas
	for j in range(n): # Columnas
		if (i == 0 and j == 0): 			# Esquina Superior Izquierda
			S[c,0] 		=	  2		#Actual
			S[c,1] 		=	 -2		#Derecha1
			S[c,2] 		= 	1		#Derecha2
			S[c,n-1] 	=  -2   #Abajo1
			S[c,2*n-1] =   1		#Abajo2
		elif (i == 0 and j < n - 2): 	# Lado Superior
			S[c,c-1] 		=	  1		#Izquierda
			S[c,c] 			=	 -1		#Actual
			S[c,c+1] 		= 	1		#Derecha
			S[c,c+n-1] 	=  -2		#Abajo1
			S[c,c+2*n-1] =   1		#Abajo2
		elif (i == 0 and j == n - 2): # Especial Superior Esquina Superior Derecha
			S[c,c-1] 			=	  1			#Izquierda
			S[c,c] 				=	 -1			#Actual
			S[c,c+n-1] 		=	 -2			#Abajo1
			S[c,c+2*n-1] 	=   1			#Abajo2
			b[c] 					=  -200		#EsquinaSD
		elif (j == 0 and i > 0 and i < n - 2):	# Lado izquierdo
			if (i == 1): # Segunda fila #Arriba
				S[c,c-(n-1)] 	=	  1
			else: 
				S[c,c-n] 	=	  1			
			S[c,c] 			=	 -1		#Actual
			S[c,c+1] 		=  -2		#Derecha1
			S[c,c+2] 		=   1		#Derecha2
			S[c,c+n] 		=   1		#Abajo
		elif (j == 0 and i == n - 2):	# Especial Izquierdo Esquina Inferior Izquierda 
			S[c,c-n] 		=	  1		#Arriba
			S[c,c] 			=	 -1		#Actual
			S[c,c+1] 		=  -2		#Derecha1
			S[c,c+2] 		=   1		#Derecha2
			b[c] 				=  -20	#EsquinaII
		elif (j == n-1 and i == 1):	# Especial Derecho Esquina Superior Derecha
			S[c,c-2]	 	=	  1			#Izquierda2
			S[c,c-1] 		=	 -2			#Izquierda1
			S[c,c] 			=  -1			#Actual
			S[c,c+n] 		=   1			#Abajo
			b[c] 				=   -200	#EsquinaSD
		elif (j == n-1 and i > 1 and i < n - 1):	# Lado Derecho
			S[c,c-2]	 	=	  1			#Izquierda2
			S[c,c-1] 		=	 -2			#Izquierda1
			S[c,c] 			=  -1			#Actual
			S[c,c-n] 		=   1			#Arriba
			if (i == n-2):				# Última fila #Abajo
				S[c,c+n-1] 	=   1
			else:
				S[c,c+n] 	=   1
		elif (j == 1 and i == n-1):	# Especial Inferior Esquina Inferior Izquierda
			S[c,c-(2*n-1)]	 	=	  1			#Arriba2
			S[c,c-(n-1)] 		=	 -2			#Arriba1
			S[c,c] 					=  -1			#Actual
			S[c,c+1] 				=   1			#Derecha
			b[c] 						=   -20		#EsquinaII
		elif (i == n-1 and j > 1 and j < n - 1):	# Lado Inferior
			S[c,c-(2*n-1)]	 	=	  1			#Arriba2
			S[c,c-(n-1)] 		=	 -2			#Arriba1
			S[c,c] 					=  -1			#Actual
			S[c,c+1] 				=   1			#Derecha
			S[c,c-1] 				=   1			#Izquierda
		elif (i == n-1 and j == n-1 ):	# Esquina Inferior Derecha
			S[c,c-(2*n-1)]	 	=	  1			#Arriba2
			S[c,c-(n-1)] 		=	 -2			#Arriba1
			S[c,c] 					=   2			#Actual
			S[c,c-1] 				=  -2			#Izquierda1
			S[c,c-2] 				=   1			#Izquierda2
		elif (i > 0 and i < n - 1 and j > 0 and j < n - 1):
			if (i == 1):							#SegundaFila #Arriba
				S[c,c-(n-1)]	=		1
			else:
				S[c,c-n]			=		1 	
			
			S[c,c-1]				=		1			#Izquierda	
			S[c,c]					=		-4		#Actual
			S[c,c+1]				=		1			#Derecha

			if (i == n-2):						#Penultima Fila #Abajo
				S[c,c+(n-1)]	=		1
			else:
				S[c,c+n]			=		1
		c = c +1
		
		if (i == 0 and j == n-1):
			c = c - 1
		if (i == n-1 and j == 0):
			c = c - 1



#==================================================================

sol = np.linalg.lstsq(S,b)[0]


nsol = np.array(sol)

nsol = np.insert(nsol, n-1, 200)
nsol = np.insert(nsol, n*(n-1), -20)
nsolsplit = np.split(nsol, n)

im = plt.imshow(nsolsplit, cmap ='hot')
plt.colorbar(im, orientation ='vertical')
plt.show()