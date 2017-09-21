
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/9ea1109f79cbb97b7c1ffa5279925674c0cd8f1f85ccfdd1cd56b5cf.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Chicago, Illinois, United States**, and the stations the data comes from are shown on the map below.

# In[50]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import pylab

import datetime
import numpy as np

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

# leaflet_plot_stations(400,'9ea1109f79cbb97b7c1ffa5279925674c0cd8f1f85ccfdd1cd56b5cf')


# In[90]:

# Obtain dataframe for years 2005-2014, and for 2015 separately
def read_data():

    df = pd.read_csv("data/C2A2_data/BinnedCsvs_d400/9ea1109f79cbb97b7c1ffa5279925674c0cd8f1f85ccfdd1cd56b5cf.csv")
    
    # remove Feb 29
    df = df[~df['Date'].str.contains("-02-29")]
    
    # add a column for day of the year
    df['Day'] = pd.DatetimeIndex(df['Date']).dayofyear
      
    # convert temperature to Celcius
    df['Data_Value'] = df['Data_Value'].apply(lambda x: x/10)
       
    dfprev = df[(df['Date']>='2005-01-01') & (df['Date']<='2014-12-31')]
    df15 = df[(df['Date']>='2015-01-01') & (df['Date']<='2015-12-31')]
    
    return dfprev, df15

dfprev, df15 = read_data()
dfprev.head()


# In[52]:

def get_record_low(df):
    '''Create a Series of record low temperatures by day of the year'''
    
    all_min_vals = df[df["Element"] == "TMIN"]
    min_val = all_min_vals.groupby('Day').min()
    min_val = min_val["Data_Value"]
    # min_val = min_val.tolist()
    
    return min_val


def get_record_high(df):
    '''Create a Series of record high temperatures by day of the year'''
    
    all_max_vals = df[df["Element"] == "TMIN"]
    max_val = all_max_vals.groupby('Day').max()
    max_val = max_val["Data_Value"]
    
    
    return max_val

type(get_record_low(dfprev))


# In[80]:

def get_plot_data():   
    dfprev, df15 = read_data()
    min_prev = get_record_low(dfprev).rename("min_prev")
    max_prev = get_record_high(dfprev).rename("max_prev")

    min_15 = get_record_low(df15).rename("min_15")
    max_15 = get_record_high(df15).rename("max_15")

    Temp = pd.concat([min_prev, min_15, max_prev, max_15],axis=1)

    # get indices where 2015 broke the all time low/high records
    broken_min = np.where(Temp["min_15"] < Temp["min_prev"], Temp["min_15"], np.nan)
    broken_max = np.where(Temp["max_15"] > Temp["max_prev"], Temp["max_15"], np.nan)
    
    return None


# In[100]:

def plot_chart():
    
    get_plot_data()
    
    plt.figure()
    plt.title("Record Temperatures in Chicago (2005-2015)")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    
    ticks = [i*30.4+15 for i in range(12)] # just to start ticks in the middle of the month
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec']
    plt.xticks( ticks, labels)

    lows = plt.plot(min_prev, 'deepskyblue', label='Record Low')
    highs = plt.plot(max_prev, 'crimson', label='Record High')

    broken_low = plt.scatter(Temp.index.values, broken_min, color='navy')
    broken_high = plt.scatter(Temp.index.values, broken_max, color='orange')

    plt.legend([broken_low, broken_high], ['2015 record low', '2015 record high'])
    plt.fill_between(Temp.index.values, Temp["min_prev"], Temp["max_prev"], color='lightgrey')
    
    return None


# In[105]:

plot_chart()
pylab.show()

