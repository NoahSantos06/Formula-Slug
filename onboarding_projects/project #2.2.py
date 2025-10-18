import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("Data/08102025Endurance1_FirstHalf.parquet")

print(df.columns)

power_current = df["ACC_POWER_CURRENT"]
power_pack_voltage = df["ACC_POWER_PACK_VOLTAGE"]
power_soc = df["ACC_POWER_SOC"]

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(power_current)
ax1.set_title("Power Current")

ax2 = fig.add_subplot(222)
ax2.plot(power_pack_voltage)
ax2.set_title("Power Pack Voltage")

ax3 = fig.add_subplot(223)
ax3.plot(power_soc)
ax3.set_title("State of Charge")

ax4 = fig.add_subplot(224)
ax4.set_title("Power Current vs Power Pack Voltage vs State of Charge")
ax4.set_xlabel("Power Current")
ax4.set_ylabel("Power Pack Voltage")
sc = ax4.scatter(power_current, power_pack_voltage, c=power_soc)
cbar = fig.colorbar(sc)
cbar.set_label("State of Charge")

plt.show()