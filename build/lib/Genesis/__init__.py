"""
Genesis

A simple library to load data science stuff without having to repeat a lot
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML
from ipywidgets import interact, IntSlider
from IPython.display import display

pd.options.display.max_columns = 35
pd.options.display.max_rows = 300

plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['figure.dpi'] = 170  # 200 e.g. is really fine, but slower

import IPython.display as ipd

plt.ion()

display(HTML("<style>.container { width:95% !important; }</style>"))


def plot_frozen(df, num_rows=30, num_columns=30, step_rows=1,
                step_columns=1):
    """
    Freeze the headers (column and index names) of a Pandas DataFrame. A widget
    enables to slide through the rows and columns.

    Parameters
    ----------
    df : Pandas DataFrame
        DataFrame to display
    num_rows : int, optional
        Number of rows to display
    num_columns : int, optional
        Number of columns to display
    step_rows : int, optional
        Step in the rows
    step_columns : int, optional
        Step in the columns

    Returns
    -------
    Displays the DataFrame with the widget
    """

    @interact(last_row=IntSlider(min=min(num_rows, df.shape[0]),
                                 max=df.shape[0],
                                 step=step_rows,
                                 description='rows',
                                 readout=False,
                                 disabled=False,
                                 continuous_update=True,
                                 orientation='horizontal',
                                 slider_color='purple'),
              last_column=IntSlider(min=min(num_columns, df.shape[1]),
                                    max=df.shape[1],
                                    step=step_columns,
                                    description='columns',
                                    readout=False,
                                    disabled=False,
                                    continuous_update=True,
                                    orientation='horizontal',
                                    slider_color='purple'))
    def _freeze_header(last_row, last_column):
        display(df.iloc[max(0, last_row - num_rows):last_row,
                max(0, last_column - num_columns):last_column])