"""
03. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
"""
import logging

logging.basicConfig(level=logging.INFO)

def soma(n1, n2, n3):
    somar = n1 + n2 + n3
    logging.info(f"{n1} + {n2} + {n3} = {somar}")

soma(1, 2, 3)