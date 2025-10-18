import matplotlib.pyplot as plt
import polars as pl

df = pl.read_parquet("Data/08102025Endurance1_FirstHalf.parquet")
df = df.filter(pl.col("VDM_GPS_Latitude") != 0).filter(pl.col("VDM_GPS_Longitude") != 0)

print(df.columns)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(df["VDM_GPS_SPEED"], label = "speed")
ax1.plot(df["ETC_STATUS_RTDS"], label= "RTDS")
ax1.set_ylabel("Speed (mph)")
ax1.legend()
# ax1.legend(["speed", "rtds"])

ax2.plot(df["VDM_GPS_Latitude"], df["VDM_GPS_Longitude"])
ax2.set_title("Track")

ax3.plot(df["ETC_STATUS_RTDS"])
ax3.set_title("RTDS")

ax4.plot(df["ACC_POWER_PACK_VOLTAGE"])
ax4.set_title("Power Pack Voltage")

plt.show()
