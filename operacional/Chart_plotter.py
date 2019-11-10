# Módulos para o matplot
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Modulos para tkinter:
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modulos para o pandas:
#from pandas.plotting import register_matplotlib_converters
import pandas as pd
#register_matplotlib_converters()

# Outros scripts:
import Path_finder as pf
import API_puller as ap

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Cotação diária
        name = ap.pull()
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data = pd.read_csv(path)
        data.loc[:, 'timestamp'] = data.loc[:, 'timestamp'].map(mdates.datestr2num)
        data = data.loc[:,['timestamp','open','high','low','close']]

        # SMA:
        name = ap.pull(function='SMA',interval='daily',series_type='close',time_period='15')
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data_sma = pd.read_csv(path)
        data_sma = data_sma.loc[0:100,['time','SMA']]
        data_sma.loc[:, 'time'] = data_sma.loc[:, 'time'].map(mdates.datestr2num)

        ax = plt.subplot()
        fig = plt.subplot()
        fig.plot(data_sma['time'], data_sma['SMA'], color='green', label='SMA5')
        candlestick_ohlc(ax, data.values, width=0.7, colorup='g', colordown='r')
        #ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_title('SMA', color='white')
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis_date()
        canvas = FigureCanvasTkAgg(ax.figure, self)
        canvas.get_tk_widget().grid(row=0,column=0)
        #canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=False)
        canvas2 = FigureCanvasTkAgg(fig.figure, self)
        canvas2.get_tk_widget().grid(row=0, column=1)
        #canvas2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=False)


        """fig = Figure(figsize = (7.5, 4.5), dpi = 100)
        ax = fig.add_subplot(111)


        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
        ax.xaxis.set_major_formatter(weekFormatter)
        candlestick_ohlc(ax, data, width=0.6)
        ax.xaxis_date()
        ax.autoscale_view()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = TOP,  fill = BOTH,  expand = False)"""


if __name__ == "__main__":
    app = App()
    app.geometry("1920x1080+51+51")
    app.title("Candlestick")
    app.mainloop()