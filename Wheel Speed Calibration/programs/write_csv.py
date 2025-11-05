import polars as pl
import matplotlib.pyplot as plt


df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30_withRPM.parquet")

 
fl = df.filter(pl.col("TPERIPH_FL_DATA_WHEELSPEED").is_not_null())
fr = df.filter(pl.col("TPERIPH_FR_DATA_WHEELSPEED").is_not_null())
br = df.filter(pl.col("TPERIPH_BR_DATA_WHEELSPEED").is_not_null())
bl = df.filter(pl.col("TPERIPH_BL_DATA_WHEELSPEED").is_not_null())

speed = df.filter(pl.col("VDM_GPS_SPEED").is_not_null())

bl_rpm = df.filter(pl.col("TPERIPH_BL_DATA_RPM").is_not_null())
br_rpm = df.filter(pl.col("TPERIPH_BR_DATA_RPM").is_not_null())



bl.select("TPERIPH_BL_DATA_WHEELSPEED").write_csv("Wheel Speed Calibration/csvs/wheel speed/back left wheel speed.csv")
br.select("TPERIPH_BR_DATA_WHEELSPEED").write_csv("Wheel Speed Calibration/csvs/wheel speed/back right wheel speed.csv")
fl.select("TPERIPH_FL_DATA_WHEELSPEED").write_csv("Wheel Speed Calibration/csvs/wheel speed/front left wheel speed.csv")
fr.select("TPERIPH_FR_DATA_WHEELSPEED").write_csv("Wheel Speed Calibration/csvs/wheel speed/front right wheel speed.csv")

bl.select("TPERIPH_BL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back left wheel rpm.csv")
br.select("TPERIPH_BR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back right wheel rpm.csv")
fr.select("TPERIPH_FR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front right wheel rpm.csv")
fl.select("TPERIPH_FL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front left wheel rpm.csv")

speed.select("VDM_GPS_SPEED").write_csv("Wheel Speed Calibration/csvs/gps speed/gps speed.csv")

# writes csvs for original data
df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30_withRPM.parquet")

front_left_wheel_speed = df["TPERIPH_FL_DATA_WHEELSPEED"]
front_right_wheel_speed = df["TPERIPH_FR_DATA_WHEELSPEED"]
back_left_wheel_speed = df["TPERIPH_BL_DATA_WHEELSPEED"]
back_right_wheel_speed = df["TPERIPH_BR_DATA_WHEELSPEED"]
gps_speed = df["VDM_GPS_SPEED"]

df.select(front_right_wheel_speed).write_csv("Wheel Speed Calibration/csvs/wheel speed/front right wheel speed original.csv")
df.select(front_left_wheel_speed).write_csv("Wheel Speed Calibration/csvs/wheel speed/front left wheel speed original.csv")
df.select(back_right_wheel_speed).write_csv("Wheel Speed Calibration/csvs/wheel speed/back right wheel speed original.csv")
df.select(back_left_wheel_speed).write_csv("Wheel Speed Calibration/csvs/wheel speed/back left wheel speed original.csv")
df.select(gps_speed).write_csv("Wheel Speed Calibration/csvs/gps speed/gps speed original.csv")
        
