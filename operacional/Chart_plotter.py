# Módulos para o matplot
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Modulos para tkinter:
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Modulos para o pandas:
from pandas.plotting import register_matplotlib_converters
import pandas as pd
register_matplotlib_converters()

# Outros scripts:
import Plotagem.operacional.Path_finder as pf
import Plotagem.operacional.API_puller as ap

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Cotação diária
        name = ap.pull()
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data = pd.read_csv(path)
        data.loc[:, 'timestamp'] = data.loc[:, 'timestamp'].map(mdates.datestr2num)
        data = data.loc[:,['timestamp','open','high','low','close']]
        self.data = data

        # Simple moving average(SMA):
        name = ap.pull(function='SMA',interval='daily',series_type='close',time_period='15')
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data_sma = pd.read_csv(path)
        data_sma = data_sma.loc[0:100,['time','SMA']]
        data_sma.loc[:, 'time'] = data_sma.loc[:, 'time'].map(mdates.datestr2num)
        self.data_sma = data_sma

        # Exponential moving average(EMA):
        name = ap.pull(function='EMA', interval='daily', series_type='close', time_period='15')
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data_ema = pd.read_csv(path)
        data_ema = data_ema.loc[0:100, ['time', 'EMA']]
        data_ema.loc[:, 'time'] = data_ema.loc[:, 'time'].map(mdates.datestr2num)
        self.data_ema = data_ema

        # Double exponential moving average(DEMA):
        name = ap.pull(function='DEMA', interval='daily', series_type='close',time_period='15')
        path = pf.find('{}.csv'.format(name), '/home/homerico/Documentos/POO2/Plotagem')
        data_macd = pd.read_csv(path)
        data_macd = data_macd.loc[0:100, ['time', 'DEMA']]
        data_macd.loc[:, 'time'] = data_macd.loc[:, 'time'].map(mdates.datestr2num)
        self.data_macd = data_macd

    def get_canvas(self,data_candle,data_metric=None,name_metric='',num=1):
        ax = plt.subplot()
        if name_metric != '':
            fig = plt.subplot()
            fig.plot(data_metric['time'], data_metric[name_metric], color='green', label=name_metric)
        candlestick_ohlc(ax, data_candle.values, width=0.7, colorup='g', colordown='r')
        #ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_title(name_metric, color='white')
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis_date()
        canvas = FigureCanvasTkAgg(ax.figure, self)
        del ax
        return canvas
        #canvas.get_tk_widget().grid(row=0,column=0)
        #canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=False)
        #canvas2 = FigureCanvasTkAgg(fig.figure, self)
        #canvas2.get_tk_widget().grid(row=1, column=0)
        #canvas2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=False)

if __name__ != "__main__":
    app = App()
    canvas_candle = app.get_canvas(data_candle=app.data)
    canvas_candle.get_tk_widget().grid(row=0,column=0)
    canvas_sma = app.get_canvas(data_candle=app.data,data_metric=app.data_sma,name_metric='SMA',num=2)
    canvas_sma.get_tk_widget().grid(row=0, column=1)
    canvas_ema = app.get_canvas(data_candle=app.data,data_metric=app.data_ema,name_metric='EMA',num=3)
    canvas_ema.get_tk_widget().grid(row=1, column=0)
    canvas_macd = app.get_canvas(data_candle=app.data,data_metric=app.data_macd,name_metric='DEMA',num=4)
    canvas_macd.get_tk_widget().grid(row=1, column=1)
    app.geometry("1000x800")
    app.title("Candlestick")
    app.mainloop()