from random import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import tkinter as tk
import pandas as pd

mass = []
sum = 0
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("величина шага")
window.geometry('400x300')
frame=Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
step_lb=Label(
    frame,
    text="введите величину шага "
)
step_lb.grid(row=0,column=0)

height_tf=Entry(
    frame,
)

def getInput():
    u=height_tf.get()
    window.destroy()
    global params
    params = [u]

height_tf.grid(row=0,column=1)

cal_btn=Button(
    frame,
    text='рассчитать',
    command = getInput   
)
cal_btn.grid(row=1,column=1)
#user_input=height_tf.get()
window.mainloop()

path = 'data.csv'

data = pd.read_csv(path)

time_of_event = list(data['time_of_event'])


last_event = time_of_event[-1]
   
steps = []
count_step = int(params[0])

for i in range(0, int(last_event), int(last_event / count_step)):
    steps.append(i)

    
  
 #Creation of plot 
fig = plt.figure(figsize=(15, 7)) 
  
#plotting the Histogram with certain intervals 
plt.hist(time_of_event, bins=steps, bottom = 0, edgecolor = 'black', color = 'lightgreen') 
plt.xlabel("time segments",fontsize=16)
plt.ylabel("events",fontsize=16)
  
#Giving title to Histogram 
plt.title("Histogram of random events") 

  
#Displaying Histogram 
plt.show() 