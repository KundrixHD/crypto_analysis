import datetime as dt

import mplfinance as mpf
import pandas as pd
import pandas_datareader as web
import threading

start = dt.datetime(2020, 6, 1)
end = dt.datetime.now()
btcusd_data = web.DataReader("BTC-USD", "yahoo", start, end)


##Display
myscreen_fx = (1)
myscreen_X = (2560 * myscreen_fx)
myscreen_Y = (1440 * myscreen_fx)
dpi_XY = (100)

mpf.plot(btcusd_data,
         type='candle',
         figsize=(myscreen_X / dpi_XY, myscreen_Y / dpi_XY),
         mav=(2, 7, 20),
         volume=True,
         style="yahoo",
         scale_padding=0.3
         )
