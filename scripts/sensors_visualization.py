import geopandas as gpd
import pandas as pd
import numpy as np
import h5py

wd = "/Users/srahmani/Library/CloudStorage/OneDrive-DelftUniversityofTechnology/Git/DCRNN_PyTorch_Saeed"


######### Turning h5 to csv #########
#h5 file path
filename = wd+'/data/metr-la_20.h5'

#read h5 file
dataset = h5py.File(filename, 'r')

#print the first unknown key in the h5 file
print(dataset.keys()) #returns df


#save the h5 file to csv using the first key df
with pd.HDFStore(filename, 'r') as d:
    df = d.get('df')
    df.to_csv('metr-la___20test.csv')

######## Creating the 20 Sensor CSV #######
# data = pd.read_csv(wd+'/data/metr-la.csv')
# ids = pd.read_csv(wd+'/data/sensor_graph/graph_sensor_ids_20.txt')
# list = ids.columns
# data_20 = pd.concat([data[data.columns[0]], data[list]], axis=1)
# data_20.to_csv(wd+'/data/metr-la_20.csv', index=False)

######## Creating the 20 Sensor h5 file #######
# data_20.to_hdf(wd+'/data/metr-la_20.h5', key='data_20', mode='w') 