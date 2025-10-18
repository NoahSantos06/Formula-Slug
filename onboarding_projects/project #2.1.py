import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("Data/08102025Endurance1_SecondHalf.parquet")

torque = df["SME_TRQSPD_Torque"]
motor_rotational_speed = df["SME_TRQSPD_Speed"]
motor_temp = df["SME_TEMP_MotorTemperature"]

print(df.columns)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(torque)
ax1.set_title("Torque")

ax2 = fig.add_subplot(222)
ax2.plot(motor_temp)
ax2.set_title("Motor Temperature")

ax3 = fig.add_subplot(223)
ax3.plot(motor_rotational_speed)
ax3.set_title("Motor Rotational Speed")

ax4 = fig.add_subplot(224)
sc4 = ax4.hexbin(torque, motor_rotational_speed, C=motor_temp, cmap='plasma')
ax4.set_title("Torque vs Motor Shaft Rotational Speed vs Car Speed")
ax4.set_xlabel("Torque")
ax4.set_ylabel("Motor Shaft Rotational Speed")
cbar = fig.colorbar(sc4)
cbar.set_label("Speed")

plt.show()