import polars as pl
import matplotlib.pyplot as plt

df_clean = pl.read_parquet("Wheel Speed Calibration/data/cleaned.parquet")
df = pl.read_parquet("Wheel Speed Calibration/data/firstDriveMCError30.parquet")

front_left_wheel_speed = df_clean["TPERIPH_FL_DATA_WHEELSPEED"]
front_right_wheel_speed = df_clean["TPERIPH_FR_DATA_WHEELSPEED"]
back_left_wheel_speed = df_clean["TPERIPH_BL_DATA_WHEELSPEED"]
back_right_wheel_speed = df_clean["TPERIPH_BR_DATA_WHEELSPEED"]

fig = plt.figure()


ax1 = fig.add_subplot(221)
ax1.plot(front_left_wheel_speed)
ax1.set_title("Front Left wheel speed")


ax2 = fig.add_subplot(222)
ax2.plot(front_right_wheel_speed)
ax2.set_title("Front right wheel speed")


ax3 = fig.add_subplot(223)
ax3.plot(back_left_wheel_speed)
ax3.set_title("back left wheel speed")


ax4 = fig.add_subplot(224)
ax4.plot(back_right_wheel_speed)
ax4.set_title("back right wheel speed")

plt.show()

