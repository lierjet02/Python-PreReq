# -*- coding: utf-8 -*-

""" The data file for this is WburgWeather.csv """

""" Write programming code to create the cleansed DataFrame here 
    using the variable name dfWeather for your DataFrame as directed 
    in the assignment.                                               """
    
"""Load pandas package"""
import pandas as pd

"""Import WburgWeather.csv"""
dfWeather = pd.read_csv('WburgWeather.csv')

"""Drop rows with NaN in the below rows"""
dfWeather.dropna(subset = ['HOURLYDRYBULBTEMPF', 'HOURLYWETBULBTEMPF', 'HOURLYDewPointTempF'],
                 inplace = True)

"""Create new columns with Celsius conversion"""
dfWeather['HOURLYDRYBULBTEMPF'] = pd.to_numeric(dfWeather['HOURLYDRYBULBTEMPF'], errors = 'coerce') #change data type to numeric
dfWeather['HOURLYDRYBULBTEMPC'] = (dfWeather['HOURLYDRYBULBTEMPF'] - 32.0) * (5 / 9)    #convert temp to celsius
dfWeather['HOURLYWETBULBTEMPC'] = (dfWeather['HOURLYWETBULBTEMPF'] - 32.0) * (5 / 9)    #convert temp to celsius
dfWeather['HOURLYDewPointTempF'] = pd.to_numeric(dfWeather['HOURLYDewPointTempF'], errors = 'coerce')   #change data type to numeric
dfWeather['HOURLYDewPointTempC'] = (dfWeather['HOURLYDewPointTempF'] - 32.0) * (5 / 9)  #convert temp to celsius

"""Clarify the VRB in HOURLYWindDirection Column"""
def windDirection(col):
    if col == 'VRB':                    #only changes elements that are VRB 
        col = 'Variable Direction'
        return col
    else:
        return col

dfWeather['HOURLYWindDirection'] = dfWeather['HOURLYWindDirection'].apply(windDirection)    #applys formula to HOURLYWindDirection column

"""Create New File for the Cleansed Data"""
dfWeather.to_csv('newWeather.csv', index = False)