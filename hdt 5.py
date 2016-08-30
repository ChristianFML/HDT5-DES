Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # ******************************************************************************
# -*- coding: cp1252 -*-
# Christian Morales - 15015
# José Luis Méndez - 15024
# Descripción: 
# ******************************************************************************

# L I B R E R I A S
import simpy
import randomA B L E S  G L O B A L E S
global 

# *****************************************************************************
# ****************** P R O C E S O S ******************************************
# *****************************************************************************
def newProcess(env, name, unit, cantRAM, io, MEMORY, INST):


init_STRT = env.now # Se inicia un nuevo proceso
	print ('El proceso %s fue creado durante las %s U.D.T' % (name, init_STRT))	# Se imprime la instruccion
	
	global time_TOT, time_PRCS, time_IO, capacidad_PRCS

	with ram.get(mem) as req:
		yield req
		init_RDY = env.now
		print ('El proceso %s ha pasado al estado ready durante las %s U.D.T.' % (name, init_RDY))

		while (ins > 0): 
			with unit.request() as req2:
				yield req2
				init_PRCS = env.now 
				print ('El proceso %s se ha empezado a procesar durante las %s U.D.T' % (name, init_PRCS))

				yield env.timeout(time_PRCS)
				exit_PRCS = env.now 
				print ('El proceso %s se ha terminado de procesar durante las %s U.D.T' % (name, exit_PRCS))

				if (ins < capacidad_PRCS):
					term_PRCS = env.now 
					print ('El proceso %s ha finalizado durante las %s U.D.T' % (name, term_PRCS))
					term_PRCS = env.now
					temp_PRCS_time = term_PRCS - init_STRT
					lista.append(temp_PRCS_time)
					time_TOT = time_TOT + temp_PRCS_time	
					ram.put(mem)	
					ins = 0		
				else:
					ins -= capacidad_PRCS	
					if (random.randint(1,2) == 1):
						with io.request() as req3:
							yield req3
							init_IO = env.now
							print ('El proceso %s ha iniciado etapa I/O durante las %s U.D.T' % (name, init_IO))

							time_Waiting_IO = random.randint(1,time_IO)
							yield env.timeout(time_Waiting_IO)
							exit_IO = env.now
							temp_PRCS_time = exit_IO - init_STRT
							lista.append(temp_PRCS_time)
							time_TOT = time_TOT + temp_PRCS_time

							print ('El proceso %s ha finalizado etapa I/O durante las %s U.D.T' % (name, exit_IO))












	

    
def proces(env, cant, cap, unit, io, RAM):
    for i in range(cant):
        MEMORY = random.randint(1,100)  #numero aleatorio entre 1 y 100
                                         #que es el numero max de memoria
        INST = random.randint(1, 10)     #numero aleatorio entre 1 y 10 para
                                         #definir cantidad de instrucciones
        nuevoP = newProcess(env, ('%s' % i), unit, cantRAM, IO, MEMORY, INST)
        env.process(nuevoP)
        tempT = random.expovariate(1.0/cap)
        yield env.timeout(tempT)

# *****************************************************************************
# ******** P A R A M S. - P A R A - S I M U L A C I O N ***********************
# *****************************************************************************

# S I M U L A C I O N
env = simpy.Environment() # Se crea el ambiente para simulación
CPU = simpy.Resource(env, capacity=1) # Un solo CPU
RAM = simpy.Container(env, capacity = 100, init=100) # Se genera la RAM con 100
IO = simpy.Resource(env, capacity=2)
# C O N S T A N T E S  Y  V A R I A B L E S - G L O B A L E S
global PROCESOS, TIMEP, INSTMAX, TOTALTIME, ARRAY
PROCESOS = 25       #cantidad de procesos a ejecutar
TIMEP = 1           #tiempo en ejecutar un proceso
INSTMAX = 1         #cantidad maxima de instrucciones posibles a ejecutar
TOTALTIME = 0.0
ARRAY = []
# R A N D O M
SEED = 42 # Genera la misma serie random
random.seed(SEED)

# D I S T.  E X P O N E N C I A L
INTERVAL = 10       #intervalo - capacidad de procesos
EXPO = random.expovariate(1.0/INTERVAL)

# ******************************************************************************
# ***************** S I M U L A C I O N ****************************************
# ******************************************************************************

# P R O C E S O S
env.process(procesamiento(env, PROCESOS, INTERVAL, CPU, IO, RAM))
    
# C O R R E R    
env.run()

# P R O M E D I O
print("Tiempo total: %f" % TOTALTIME)
PROM = (TOTALTIME/PROCESOS)
print("El promedio de tiempo de procesamiento es: %f" % PROM)

# D E S V.  E S T A N D A R
temporal = 0        #Variable temporal almacenará la sumatoria
#Con un arreglo se hará la sumatoria de datos
for i in ARRAY:
    temporal += (i-promedio)**2     #La sumatoria de:
                                    #cada dato - el promedio elevado al cuadrado

DESV = (temporal/ (procesos-1) )**0.5       #Raíz cuadrada de la sumatoria anterior
                                            #partida n-1
print "La desviación estándar es: ", DESV
