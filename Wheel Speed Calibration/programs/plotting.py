import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_53.parquet")

back_left_wheel_speed = df["TPERIPH_BL_DATA_WHEELSPEED"]
back_right_wheel_speed = df["TPERIPH_BR_DATA_WHEELSPEED"]
front_left_wheel_speed = df["TPERIPH_FL_DATA_WHEELSPEED"]
front_right_wheel_speed = df["TPERIPH_FR_DATA_WHEELSPEED"]


fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(back_left_wheel_speed)
ax1.set_title("back left wheel speed")

ax2 = fig.add_subplot(222)
ax2.plot(back_right_wheel_speed)
ax2.set_title("back right wheel speed")

ax3 = fig.add_subplot(223)
ax3.plot(front_left_wheel_speed)
ax3.set_title("front left wheel speed")

ax4 = fig.add_subplot(224)
ax4.plot(front_right_wheel_speed)
ax4.set_title("front right wheel speed")

plt.show()