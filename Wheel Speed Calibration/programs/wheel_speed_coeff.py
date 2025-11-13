import polars as pl
import matplotlib.pyplot as plt
import numpy as np


df = pl.read_parquet("Wheel Speed Calibration/parquets/1108-11_54_filtered.parquet")

back_left_wheel_speed = df["TPERIPH_BL_DATA_WHEELSPEED"]
back_right_wheel_speed = df["TPERIPH_BR_DATA_WHEELSPEED"]
front_left_wheel_speed = df["TPERIPH_FL_DATA_WHEELSPEED"]
front_right_wheel_speed = df["TPERIPH_FR_DATA_WHEELSPEED"]
gps_speed = df["VDM_GPS_SPEED"]
motor_rpm = df["SME_TRQSPD_Speed"]

# wheel_speed * x == rpm

average = 0
n = 0
total = 0

for i in range(df.height):

    n += 1

    if front_left_wheel_speed[i] == 0:

        continue
    
    total += ((gps_speed[i] * (63360/60) * (1/(16*np.pi))) / front_left_wheel_speed[i])

average = total / n

print(average)

