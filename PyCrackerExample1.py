import os
from PyCrackerBase import PyCracker

cracker = PyCracker()
cracker.setDebug(1)
cracker.setThreads(1)
cracker.setConfig(os.path.abspath(os.path.dirname(__file__))+'/configs/origin.py')

