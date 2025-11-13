import matplotlib.pyplot as plt
import polars as pl
import numpy as np

df = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_53_filtered.parquet")

back_left_wheel_speed = df["TPERIPH_BL_DATA_WHEELSPEED"]
back_right_wheel_speed = df["TPERIPH_BR_DATA_WHEELSPEED"]
front_left_wheel_speed = df["TPERIPH_FL_DATA_WHEELSPEED"]
front_right_wheel_speed = df["TPERIPH_FR_DATA_WHEELSPEED"]
gps_speed = df["VDM_GPS_SPEED"]
motor_rpm = df["SME_TRQSPD_Speed"]

fig = plt.figure()

ax2 = fig.add_subplot(111)
ax2.plot(gps_speed * (63360/60) * (1/(16*np.pi)), alpha=0.6, label="gps speed -> rpm")
ax2.plot(front_left_wheel_speed * 0.8452494744062437, alpha=0.6, label="fl wheel speed -> rpm")
ax2.set_title("gps speed -> rpm vs fl wheel speed -> rpm")
ax2.legend()

plt.show()