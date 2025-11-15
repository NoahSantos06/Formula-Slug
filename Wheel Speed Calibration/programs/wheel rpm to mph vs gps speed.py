import matplotlib.pyplot as plt
import polars as pl
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

fig = plt.figure()

wheel_speed_coeff = 0.8452494744062437
rpm_to_mph_coeff = (2 * np.pi * 8 * 60) / 63360

ax1 = fig.add_subplot(221)
# ax1.scatter(df_1108_11_54[fl_wheel_speed] * wheel_speed_coeff, df_1108_11_54[motor_rpm] * (12/41))
ax1.plot(df_1108_11_54[fl_wheel_speed] * wheel_speed_coeff * rpm_to_mph_coeff, label="fl wheel speed to rpm")
ax1.plot(df_1108_11_54[gps_speed], label="gps speed")
ax1.set_title("wheel speed conversion vs gps speed for 1108-11_54")
ax1.legend()

ax2 = fig.add_subplot(222)
# ax2.scatter(df_1109_4_26[fl_wheel_speed] * wheel_speed_coeff, df_1109_4_26[motor_rpm] * (12/41))
ax2.plot(df_1109_4_26[fl_wheel_speed] * wheel_speed_coeff * rpm_to_mph_coeff, label="fl wheel speed to rpm to mph")
ax2.plot(df_1109_4_26[gps_speed], label="gps speed")
ax2.set_title("wheel speed conversion vs gps speed for 1109-4_26")
ax2.legend()

ax3 = fig.add_subplot(223)
# ax3.scatter(df_1109_4_30[fl_wheel_speed] * wheel_speed_coeff, df_1109_4_30[motor_rpm] * (12/41))
ax3.plot(df_1109_4_30[fl_wheel_speed] * wheel_speed_coeff * rpm_to_mph_coeff, label="fl wheel speed to rpm to mph")
ax3.plot(df_1109_4_30[gps_speed], label="gps speed")
ax3.set_title("wheel speed conversion to mph vs gps speed for 1109-4_30")
ax3.legend()

ax4 = fig.add_subplot(224)
# ax4.scatter(df_1109_4_53[fl_wheel_speed] * wheel_speed_coeff, df_1109_4_53[motor_rpm] * (12/41))
ax4.plot(df_1109_4_53[fl_wheel_speed] * wheel_speed_coeff * rpm_to_mph_coeff, label="fl wheel speed to rpm to mph")
ax4.plot(df_1109_4_53[gps_speed], label="gps speed")
ax4.set_title("wheel speed conversion to mph vs gps speed for 1109-4_53")
ax4.legend()

plt.show()