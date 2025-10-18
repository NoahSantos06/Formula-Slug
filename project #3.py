import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("Data/08102025Endurance1_FirstHalf.parquet")

# going based of coast-down method

# m*(dv/dt) = (-1/2)pCdA(v^2) - mgCrr - mgsin0
# dv/dt = -((1/2m)(v^2)-g(Crr+sin0))
# Y = dv/dt 
# X = v^2
# Find Linear Regression Y = aX + b
# a = (-p/2m)CdA
# CdA = -(2m/p)a

speed = df["VDM_GPS_SPEED"].to_numpy()
time = df["VDM_UTC_TIME_SECONDS"].to_numpy()
speed /= 3.6 # converts to m/s

# variables
m = 230 # average weight for a FSAE car in kg
p = 1.225 # altitude was mostly ~ 15 so air density is typically 1.225 

# estimates the time evenly from 0 - 21 seconds for dt
# the actual time dataset isn't increasing so np.gradient has an error creating the derivative array
dt = (time[-1] - time[0]) / len(time)
# np.gradient finds the derivative of dvdt, edge_order is for more accurate derivative at the edges
dvdt = np.gradient(speed, dt, edge_order=2)

#converts it to a numpy array and squares every element so it becomes v^2 instead of v
v2 = np.array(speed.tolist())**2

#converts v2 into a 2D column vector [100, 225, 400] --> [[100], [225], [400]]
#scikit-learn needs a 2d input in order to graph the linear regression
X = v2.reshape(-1,1)

#converts dvdt to numpy array
Y = np.array(dvdt)

# finds the slope as needed to find CdA
model = LinearRegression()
model.fit(X,Y)

#slope
a = model.coef_[0]

#calculates CdA using the slope, air density, and mass of the car
CdA = -(((2 * m) / p) * a)

print(f"Estimated Drag Coefficient * Cross Sectional Area: {CdA}")
