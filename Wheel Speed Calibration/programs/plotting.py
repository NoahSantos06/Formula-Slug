import polars as pl
import matplotlib.pyplot as plt

bl = pl.read_parquet("Wheel Speed Calibration/parquets/TPERIPH_BL_DATA_RPM_TO_MPH.parquet")
br = pl.read_parquet("Wheel Speed Calibration/parquets/TPERIPH_BR_DATA_RPM_TO_MPH.parquet")
trq = pl.read_parquet("Wheel Speed Calibration/parquets/SME_TRQSPD_Speed.parquet")

gps_sliced = pl.read_parquet("Wheel Speed Calibration/parquets/speed_sliced.parquet")
gps = pl.read_parquet("Wheel Speed Calibration/parquets/speed.parquet") 

back_left_wheel_rpm_filtered = bl["TPERIPH_BL_DATA_RPM"]
back_left_wheel_rpm_to_mph_filtered = bl["TPERIPH_BL_DATA_RPM_TO_MPH"]
back_left_wheel_speed_filtered = bl["TPERIPH_BL_DATA_WHEELSPEED"]

back_right_wheel_rpm_filtered = br["TPERIPH_BR_DATA_RPM"]
back_right_wheel_speed_filtered = br["TPERIPH_BR_DATA_WHEELSPEED"]

gps_sliced_speed = gps_sliced["VDM_GPS_SPEED"]
gps_speed = gps["VDM_GPS_SPEED"]

torque_speed = trq["SME_TRQSPD_Speed"]

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(gps_sliced_speed, label="gps speed (mph)")
ax1.set_title("GPS SPEED VS BACK LEFT WHEEL RPM")
ax1.plot(back_left_wheel_rpm_filtered, label="bl wheel rpm")
ax1.set_xlim(0, 1000)
ax1.legend()


ax2 = fig.add_subplot(222)
ax2.plot(back_left_wheel_rpm_filtered, label="back left wheel rpm")
ax2.set_title("back left wheel rpm")
ax2.legend()
ax2.set_xlim(0, 1000)


ax3 = fig.add_subplot(223)
ax3.plot(back_right_wheel_rpm_filtered, label="rpm")
ax3.plot(gps_speed, label="gps speed")
ax3.set_title("back right wheel rpm")
ax3.legend()
ax3.set_xlim(0, 1000)

ax4 = fig.add_subplot(224)
ax4.plot(torque_speed, label="motor rpm")
ax4.set_title("motor rpm")
ax4.set_xlim(0, 5000)
ax4.legend()

plt.show()
