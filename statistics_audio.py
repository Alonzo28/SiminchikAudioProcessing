import numpy
import csv
import pandas as pd
import commands
import os

# archivo: audio 
def create_csv(archivo):

	name_file=archivo.split('.')
	stat1=commands.getstatusoutput('sox --i '+archivo ) #obtaining the statistics
	stat2=commands.getstatusoutput("sox " + archivo + "  -n stat") #obtaining the statistics
	f=open("fichero_"+name_file[0]+"-stat.txt","w")
	f.write(stat1[1]+stat2[1])
	f.close()

	datos = [ [0 for columna in range(0,2)] for fila in range (0,24)] #creating a warehouse
	i=0
	while i<24:
		with open("fichero_"+name_file[0]+"-stat.txt", "r") as f:	
			lines = f.readlines()
		   	newline=str(lines[i])
		   	
		   	firtline=newline[0:17]
		   	
		   	dataline= newline[17:500]
			j=0	
			datos[i][j] = firtline      #saving type of information
			datos[i][j+1] = dataline    #saving data of the type ofinformation
			i=i+1
	dat = numpy.matrix(datos) #convert to matrix
	wow=pd.DataFrame(dat)
	wow.to_csv('estadisticas_'+name_file[0]+'.csv', delimiter=":") # exporting to csv
	os.remove("fichero_"+name_file[0]+"-stat.txt")
