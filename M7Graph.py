# -*- coding: utf-8 -*-
""" The data file for this is ozone.csv """

""" Write programming code using the variable names as directed 
    in the assignment.                                          """

"""Imports both packages needed for the assignment"""
import pandas as pd
import matplotlib.pyplot as plt

"""Reads the csv into a dataframe"""
df_oz = pd.read_csv('ozone.csv')

"""Ozone and Temperature have the highest correlation
    while wind and radiation have the lowest correlation"""
dfCorr = df_oz.corr()

"""Creates two subplots"""
fig,ax = plt.subplots(1, 2)

"""Creates the individual plots and sets the titles and axes labels"""
ax[0].scatter(df_oz['temperature'], df_oz['ozone'], alpha = .5, s = 150)
ax[1].scatter(df_oz['wind'], df_oz['radiation'], alpha = .5, s = 150)
ax[0].xaxis.set_label_text('Temperature (degrees F)', fontsize = 16)
ax[0].yaxis.set_label_text('Ozone Level', fontsize = 16)
ax[1].xaxis.set_label_text('Wind Speed', fontsize = 16)
ax[1].yaxis.set_label_text('Radiation', fontsize = 16)
ax[0].set_title('Ozone Level vs Temperature (Highest Correlation)', fontsize = 20)
ax[1].set_title('Radiation vs Wind Speed (Lowest Correlation', fontsize = 20)

fig.set_size_inches(20, 10)

"""Sets the extent of the two charts to whats inside the axes"""
plot1 = ax[0].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
plot2 = ax[1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())

"""Saves the individual figures by extending the reach of the 
    plots extent"""
fig.savefig('ozHi.jpg', bbox_inches = plot1.expanded(1.23, 1.2))
fig.savefig('ozLo.jpg', bbox_inches = plot2.expanded(1.23, 1.2))

plt.show()  #shows the plots