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


start = env.now # Se inicia un nuevo proceso
	print ("proceso:",name," udt:", strart) # Se imprime la instruccion
	
	global TOTALTIME, TIMEP, tiempoIO, procesos

	with cantRAM.get(MEMORY) as firstRequest:
		yield firstRequest
		ready = env.now
		print ("proceso:",name," udt:", ready )

		while (INST > 0): 
			with unit.request() as secondRequest:
				yield secondRequest
				procesosInit = env.now 
				print ("proceso:",name," udt:", procesosInit)

				yield env.timeout(TIMEP)
				procesosEnd = env.now 
				print ("proceso:",name," udt:", procesosEnd)

				if (INST < procesos):
					terminated = env.now 
					print ("proceso:",name," udt:", terminated)
					terminated = env.now
					TIMEP1 = terminated - start
					ARRAY.append(temp_PRCS_time)
					TOTALTIME = TOTALTIME + TIMEP1
					cantRAM.put(MEMORY)	
					INST = 0		
				else:
					INST -= procesos	
					if (random.randint(1,2) == 1):
						with io.request() as thirdRequest:
							yield thirdRequest
							ioInit = env.now
							print ("proceso:",name," udt:", ioInit)

							lookIO = random.randint(1,tiempoIO)
							yield env.timeout(lookIO)
							endIO = env.now
							temp_PRCS_time = endIO - start
							ARRAY.append(temp_PRCS_time)
							TOTALTIME = TOTALTIME + TIMEP1

							print ("proceso:",name," udt:", exit_IO)




):








	

    
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
