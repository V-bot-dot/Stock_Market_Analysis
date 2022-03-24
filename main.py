#importing all the necessary packages for this project.
import PyQt5

import numpy as np
import pandas as pd  #for basic data manipulation
from pandas import Grouper, DataFrame
import quandl         #for real time stocks data.
import matplotlib.pyplot as plt   #for plotting
from tkinter import *    #for python GUI
import seaborn as sns    #for plotting
from pandastable import Table, TableModel   #for linking pandas DataFrame with tkinter 
%matplotlib qt

def go1():

    compName = c.get()
    if compName == "MRF Ltd":
        my_data = quandl.get("BSE/BOM539397", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName == "3M India Ltd":
        my_data = quandl.get("BSE/BOM523395", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName == "Honeywell Automaton India Ltd":
        my_data = quandl.get("BSE/BOM517174", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-06-26")
    elif compName == "Page Industries Ltd":
        my_data = quandl.get("BSE/BOM532827", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName == "Eicher Motors Ltd":
        my_data = quandl.get("BSE/BOM505200", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="2007-03-16")
    elif compName == "Shree cement Ltd":
        my_data = quandl.get("BSE/BOM500387", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-10-26")
    elif compName == "Bosch Ltd":
        my_data = quandl.get("BSE/BOM500530", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    elif compName == "Nestle India Ltd":
        my_data = quandl.get("BSE/BOM500790", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName == "Procter and Gamble Ltd":
        my_data = quandl.get("BSE/BOM500459", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName == "Tasty Bite Eatables Ltd":
        my_data = quandl.get("BSE/BOM519091", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    
    to_plot = my_data
    my_data = my_data.reset_index()
    my_data = my_data[["Date", "Open", "Close", "High", "Low", "No. of Shares", "No. of Trades"]]
    graph(to_plot)
    
    # pandastable code.
    class TestApp(Frame):
        """Basic test frame for the table"""
        def __init__(self, parent=None):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.master
            self.main.geometry('800x600')
            self.main.title('Table app')
            f = Frame(self.main)
            f.pack(fill=BOTH,expand=1)
            df = my_data
            self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
            pt.show()
            return

    app = TestApp()
    #launch the app
    app.mainloop()
    
    
    def comp():
    p=Tk()
    p.geometry("800x200")
    p.title("Comparing companies")
    frame1=LabelFrame(p,padx=50,pady=30)
    frame1.pack(padx=10,pady=10)
    global comp1
    comp1=StringVar(p)
    comp1.set("company 1 here")
    drop1=OptionMenu(frame1,comp1,*Lis)
    drop1.grid(row=0,column=1)
    Label2=Label(frame1,text="Company name 1",padx=20,pady=25)
    Label2.grid(row=0,column=0)
    
    global comp2
    comp2=StringVar(p)
    comp2.set("Company 2 here")

    drop2=OptionMenu(frame1,comp2,*Lis)
    drop2.grid(row=0,column=3)
    Label3=Label(frame1,text="Company name 2",padx=20,pady=25)
    Label3.grid(row=0,column=2)
    button2=Button(frame1,text="Go---> " ,padx=20,pady=10, command = graph2)
    button2.grid(row=1,column=0,columnspan=4)
    p.mainloop()
    
    
    
    def graph(my_data):
    plt.figure(figsize=(8, 4))
    # sns.regplot(x = my_data["High"], y = my_data["Low"])
    plt.plot(my_data["High"], label = "High")
    plt.plot(my_data["Low"], label = "Low")
    plt.legend()
def graph2():
    compName1 = comp1.get()
    if compName1 == "MRF Ltd":
        my_data1 = quandl.get("BSE/BOM539397", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName1 == "3M India Ltd":
        my_datad1 = quandl.get("BSE/BOM523395", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName1 == "Honeywell Automaton India Ltd":
        my_data1 = quandl.get("BSE/BOM517174", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-06-26")
    elif compName1 == "Page Industries Ltd":
        my_data1 = quandl.get("BSE/BOM532827", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName1 == "Eicher Motors Ltd":
        my_data1 = quandl.get("BSE/BOM505200", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="2007-03-16")
    elif compName1 == "Shree cement Ltd":
        my_data1 = quandl.get("BSE/BOM500387", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-10-26")
    elif compName1 == "Bosch Ltd":
        my_data1 = quandl.get("BSE/BOM500530", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    elif compName1 == "Nestle India Ltd":
        my_data1 = quandl.get("BSE/BOM500790", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName1 == "Procter and Gamble Ltd":
        my_data1 = quandl.get("BSE/BOM500459", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName1 == "Tasty Bite Eatables Ltd":
        my_data1 = quandl.get("BSE/BOM519091", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    
    compName2 = comp2.get()
    if compName2 == "MRF Ltd":
        my_data2 = quandl.get("BSE/BOM539397", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName2 == "3M India Ltd":
        my_data2 = quandl.get("BSE/BOM523395", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName2 == "Honeywell Automaton India Ltd":
        my_data2 = quandl.get("BSE/BOM517174", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-06-26")
    elif compName2 == "Page Industries Ltd":
        my_data2 = quandl.get("BSE/BOM532827", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName2 == "Eicher Motors Ltd":
        my_data2 = quandl.get("BSE/BOM505200", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="2007-03-16")
    elif compName2 == "Shree cement Ltd":
        my_data2 = quandl.get("BSE/BOM500387", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-10-26")
    elif compName2 == "Bosch Ltd":
        my_data2 = quandl.get("BSE/BOM500530", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    elif compName2 == "Nestle India Ltd":
        my_data2 = quandl.get("BSE/BOM500790", authtoken="XEzc8Qx5FsuaVTCe1Ern")
    elif compName2 == "Procter and Gamble Ltd":
        my_data2 = quandl.get("BSE/BOM500459", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1991-01-03")
    elif compName2 == "Tasty Bite Eatables Ltd":
        my_data2 = quandl.get("BSE/BOM519091", authtoken="XEzc8Qx5FsuaVTCe1Ern", start_date="1992-03-02")
    fig, axs = plt.subplots(2, 2)
    fig.set_figheight(10)
    fig.set_figwidth(10)
    axs[0, 0].plot(my_data1["High"], label = comp1.get())
    axs[0, 0].plot(my_data2["High"], label = comp2.get())
    axs[0, 0].set_title('High values')
    axs[0, 0].legend()
    axs[0, 1].plot(my_data1["Low"], label = comp1.get())
    axs[0, 1].plot(my_data2["Low"], label = comp2.get())
    axs[0, 1].set_title('Low values')
    axs[0, 1].legend()
    axs[1, 0].plot(my_data1["Open"], label = comp1.get())
    axs[1, 0].plot(my_data2["Open"], label = comp2.get())
    axs[1, 0].set_title('Opening values')
    axs[1, 0].legend()
    axs[1, 1].plot(my_data1["Close"], label = comp1.get())
    axs[1, 1].plot(my_data2["Close"], label = comp2.get())
    axs[1, 1].set_title('Closing values')
    axs[1, 1].legend()

    for ax in axs.flat:
        ax.set(xlabel='timeline', ylabel='Value')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()
        
   
   r=Tk()
r.geometry("800x600")
r.title("Stocks analysis")
frame=LabelFrame(r,padx=50,pady=30)
frame.pack(padx=10,pady=10)
global c
c=StringVar()
c.set("DefaultValue")
Lis=["MRF Ltd","3M India Ltd","Honeywell Automaton India Ltd","Page Industries Ltd","Eicher Motors Ltd","Shree cement Ltd","Bosch Ltd","Nestle India Ltd","Procter and Gamble Ltd","Tasty Bite Eatables Ltd"]
drop=OptionMenu(frame,c,*Lis)
drop.grid(row=0,column=1)
Label1=Label(frame,text="Company names",padx=20,pady=25)
Label1.grid(row=0,column=0)
button1=Button(frame,text="GO---> ",padx=20,pady=10,command=go1)
button1.grid(row=1,column=0)
button2=Button(frame,text="Compare",padx=20,pady=10,command=comp)
button2.grid(row=1,column=1)

r.mainloop()
