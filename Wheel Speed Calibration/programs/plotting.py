import polars as pl
import matplotlib.pyplot as plt

bl = pl.read_parquet("bl rpm")
br = pl.read_parquet("Wheel Speed Calibration/parquets/br.parquet")
gps = pl.read_parquet("Wheel Speed Calibration/parquets/speed.parquet")
df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30.parquet")
rpm = pl.read_parquet("Wheel Speed Calibration/parquets/analog to wheel rpm.parquet")


back_left_wheel_RPM = bl["TPERIPH_BL_DATA_RPM"]
back_left_wheel_speed = bl["TPERIPH_BL_DATA_RPM"]
back_right_wheel_speed = br["TPERIPH_BR_DATA_WHEELSPEED"]
gps_speed = gps["VDM_GPS_SPEED"]
back_left_wheel_rpm = rpm["TPERIPH_BL_DATA_RPM"]
back_right_wheel_rpm = rpm["TPERIPH_BL_DATA_RPM"]



fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(gps_speed)
ax1.set_title("GPS SPEED")

ax2 = fig.add_subplot(222)
ax2.plot(back_left_wheel_RPM)
ax2.set_title("BACK LEFT WHEEL RPM")

ax3 = fig.add_subplot(223)
ax3.plot(back_left_wheel_speed)
ax3.set_title("BACK LEFT WHEEL SPEED")

ax4 = fig.add_subplot(224)
ax4.plot(back_right_wheel_speed)
ax4.set_title("BACK RIGHT WHEEL SPEED")
plt.show()