# import everything from random so I dont need to write random first
import random

def randomInput():
    input_For_Circuits = [0,1]
    final_Input = random.choice(input_For_Circuits)
    return final_Input

# purpose of function: conversion between true and false
def converseionOfBoolean(boolean):
    match boolean:
        case 0:
            return False
        case 1:
            return True
        case _:
            return "Huh?"


# purpose of function: Recreate the and gate
def andGate(A, B):
    Z = A * B

    if Z > 1:
        Z = 1

    match Z:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return "Huh?"


# purpose of function: Recreate the or gate
def orGate(A, B):
    Z = A + B

    if Z > 1:
        Z = 1

    match Z:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return "Huh?"


# purpose of function: Recreate the not gate
def notGate(A):
    match A:
        case 0:
            return 1
        case 1:
            return 0
        case _:
            return "Huh?"


# purpose of function: Recreate the xor gate
def xorGate(A, B):
    Z = A * notGate(B) + notGate(A) * B

    match Z:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return "Huh?"


# tilstande = [0, 1]

# number = 1000

# udregnings_liste = []

# for i in range(number):
#     # choice is an inbuilt function of the random package
#     A = random.choice(tilstande)

#     # choice is an inbuilt function of the random package
#     B = random.choice(tilstande)

#     # Classical boolean circuit
#     # Først skal en not(A) og en B igennnem en And operator
#     result_C = andGate(notGate(A), B)
#     # Så skal en A og en not(B) igennem en And operator
#     result_D = andGate(A, notGate(B))

#     # Så skal disse to resultater igennem en or operator0
#     endelige_result = orGate(result_C, result_D)

#     # nu converter man værdien til falsk eller true
#     endelige_result = converseionOfBoolean(endelige_result)

#     # og man tilføjer værdien til udregnings listen
#     udregnings_liste.append(endelige_result)

# mængdeAfTrue = udregnings_liste.count(True)
# mængdeAfFalse = udregnings_liste.count(False)

# print(mængdeAfTrue,mængdeAfFalse)