import polars as pl
import matplotlib.pyplot as plt

bl = pl.read_parquet("Wheel Speed Calibration/parquets/back left wheel rpm filtered.parquet")
br = pl.read_parquet("Wheel Speed Calibration/parquets/back right wheel rpm filtered.parquet")
gps = pl.read_parquet("Wheel Speed Calibration/parquets/VDM_GPS_SPEED no nulls.parquet")


back_left_wheel_rpm_filtered = bl["TPERIPH_BL_DATA_RPM"]
back_right_wheel_rpm_filtered = br["TPERIPH_BL_DATA_RPM"]
gps_speed = gps["VDM_GPS_SPEED"]


fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(gps_speed)
ax1.set_title("GPS SPEED VS BACK LEFT WHEEL RPM")
ax1.plot(back_left_wheel_rpm_filtered)
ax1.set_xlim(0, 1000)


ax2 = fig.add_subplot(222)
ax2.plot(gps_speed)
ax2.set_title("GPS SPEED")
ax2.set_xlim(0, 1000)

ax3 = fig.add_subplot(223)
ax3.plot(back_left_wheel_rpm_filtered)
ax3.set_title("BACK LEFT WHEEL RPM ")
ax3.set_xlim(0, 1000)

# plt.show()
plt.tight_layout()
plt.savefig("wheel_speed_plot.png")  # Save instead of show()
print("✅ Plot saved as wheel_speed_plot.png")
