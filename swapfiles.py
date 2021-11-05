import os
import shutil


def swapFiles():
    swap1 = input("Enter the first file to swap: ")
    swap2 = input("Enter the second file to swap: ")
    with open(swap1, 'r') as a:
        data_a = a.read()
    with open(swap2, 'r') as b:
        data_b = b.read()
    with open(swap1, 'w') as a:
        a.write(data_b)
    with open(swap2, 'w') as b:
        b.write(data_a)

swapFiles()