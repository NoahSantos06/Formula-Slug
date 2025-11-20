import polars as pl
import matplotlib.pyplot as plt
import numpy as np


df_1108_11_54 = pl.read_parquet("Wheel Speed Calibration/parquets/1108-11_54_filtered.parquet")
df_1109_4_26 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_26_filtered.parquet")
df_1109_4_30 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_30_filtered.parquet")
df_1109_4_53 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_53_filtered.parquet")

bl_wheel_speed = "TPERIPH_BL_DATA_WHEELSPEED"
br_wheel_speed = "TPERIPH_BR_DATA_WHEELSPEED"
fr_wheel_speed = "TPERIPH_FR_DATA_WHEELSPEED"
fl_wheel_speed = "TPERIPH_FL_DATA_WHEELSPEED"
gps_speed = "VDM_GPS_SPEED"
motor_rpm = "SME_TRQSPD_Speed"

# wheel_speed * x == rpm
def average(df, wheel_speed, total):
    
    for i in range(df.height):

        if df[wheel_speed][i] != 0:

            total += ((df[gps_speed][i] * (63360/60) * (1/(16*np.pi))) / df[wheel_speed][i])

    return total / df.height
    

df_1108_11_54_fl_average = average(df_1108_11_54, fl_wheel_speed, 0)
df_1108_11_54_fr_average = average(df_1108_11_54, fr_wheel_speed, 0)
df_1108_11_54_bl_average = average(df_1108_11_54, bl_wheel_speed, 0)
df_1108_11_54_br_average = average(df_1108_11_54, br_wheel_speed, 0)

df_1109_4_30_fl_average = average(df_1109_4_30, fl_wheel_speed, 0)
df_1109_4_30_fr_average = average(df_1109_4_30, fr_wheel_speed, 0)
df_1109_4_30_bl_average = average(df_1109_4_30, bl_wheel_speed, 0)
df_1109_4_30_br_average = average(df_1109_4_30, br_wheel_speed, 0)

df_1109_4_53_fl_average = average(df_1109_4_53, fl_wheel_speed, 0)
df_1109_4_53_fr_average = average(df_1109_4_53, fr_wheel_speed, 0)
df_1109_4_53_bl_average = average(df_1109_4_53, bl_wheel_speed, 0)
df_1109_4_53_br_average = average(df_1109_4_53, br_wheel_speed, 0)

# print(df_1108_11_54_bl_average)
# print(df_1108_11_54_br_average)
# print(df_1108_11_54_fl_average)
# print(df_1108_11_54_fr_average)

# print()

# print(df_1109_4_30_bl_average)
# print(df_1109_4_30_fl_average)
# print(df_1109_4_30_fr_average)
# print(df_1109_4_30_fl_average)

# print()

# print(df_1109_4_53_fr_average)
# print(df_1109_4_53_fl_average)
# print(df_1109_4_53_bl_average)
# print(df_1109_4_53_br_average)

df_1109_4_53_average = (df_1109_4_53_fr_average + df_1109_4_53_br_average + df_1109_4_53_fl_average + df_1109_4_53_bl_average) / 4
df_1109_4_30_average = (df_1109_4_30_br_average + df_1109_4_30_bl_average + df_1109_4_30_fr_average + df_1109_4_30_fl_average) / 4
df_1108_11_54_average = (df_1108_11_54_bl_average + df_1108_11_54_fr_average + df_1108_11_54_fl_average + df_1108_11_54_br_average) / 4

# print(df_1108_11_54_average)
# print(df_1109_4_30_average)
# print(df_1109_4_53_average)

coeff = (df_1108_11_54_average + df_1109_4_30_average + df_1108_11_54_average) / 3

print(coeff)
