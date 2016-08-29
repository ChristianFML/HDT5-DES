# ******************************************************************************
# -*- coding: cp1252 -*-
# Christian Morales - 15015
# José Luis Méndez - 15024
# Descripción: 
# ******************************************************************************

# L I B R E R I A S
import simpy
import random

# V A R I A B L E S  G L O B A L E S
global 

# *****************************************************************************
# ****************** P R O C E S O S ******************************************
# *****************************************************************************
def proces(env, name, )

# *****************************************************************************
# ******** P A R A M S. - P A R A - S I M U L A C I O N ***********************
# *****************************************************************************

# S I M U L A C I O N

env = simpy.Environment() # Se crea el ambiente para simulación
CPU = simpy.Resource(env, capacity=1) # Un solo CPU
RAM = simpy.Container(env, capacity = 100, init=100) # Se genera la RAM con 100

# R A N D O M
SEED = 42 # Genera la misma serie random
random.seed(SEED)

# D I S T.  E X P O N E N C I A L
INTERVAL = 10
EXPO = random.expovariate(1.0/INTERVAL)

# ******************************************************************************
# ***************** S I M U L A C I O N ***************************************
# ******************************************************************************

# P R O C E S O S
for i in range(25):
    env.process(proces(env, 'Proceso %d' % i))
    
# C O R R E R    
env.run()

# P R O M E D I O


# D E S V.  E S T A N D A R

