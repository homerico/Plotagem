import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import Path_finder as pf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

path = pf.find('cotacao.csv','/home/homerico/Documentos/POO2/Plotagem')
data = pd.read_csv(path)

root = tk.Tk()

figure1 = plt.Figure(figsize=(10, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
data['open'].plot(legend=True, ax=ax1)
data['close'].plot(legend=True, ax=ax1)
data['high'].plot(legend=True, ax=ax1)
ax1.set_title('Open X Close X High')
"""
figure1 = plt.Figure(figsize=(10, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
data['open'].plot(legend=True, ax=ax1)
data['close'].plot(legend=True, ax=ax1)
ax1.set_title('Open X Close X High')
"""


root.mainloop()