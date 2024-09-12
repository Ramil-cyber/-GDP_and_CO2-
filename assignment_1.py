import pandas as pd

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
columns = [
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]

import seaborn.objects as so
import seaborn as sns
from matplotlib import style
import numpy as np


# This is the plot
columns = [
    "Country Name",
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
]
wdi["Log GDP Per Capita"] = np.log(wdi["GDP per capita (constant 2010 US$)"])
my_chart = (
    so.Plot(
        wdi, x="Log GDP Per Capita", y="Mortality rate, infant (per 1,000 live births)"
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="GDP and Infant Mortality")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)
my_chart.show()
