import pandas as pd
import numpy as np

def my_print(s: str):
    print(s)
    print("test change")
   
def add_local_file(c):
    print("modify origin function")
    print(c)

def function_from_origin(a):
    return a+3

def add_new_function_from_origin(b):
    return b

def add_second_local_fun():
    return 

