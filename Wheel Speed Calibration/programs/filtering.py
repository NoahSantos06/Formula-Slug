import polars as pl
import matplotlib.pyplot as plt

df = pl.read_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\firstDriveMCError30.parquet")


#  filters all null values in each column
# done seperately so it doesn't mess with different columns in each parquet file
fl = df.filter(
    pl.col("TPERIPH_FL_DATA_WHEELSPEED").is_not_null()
)

fr = df.filter(
    pl.col("TPERIPH_FR_DATA_WHEELSPEED").is_not_null()
)

br = df.filter(
    pl.col("TPERIPH_BR_DATA_WHEELSPEED").is_not_null()
)

bl = df.filter(
    pl.col("TPERIPH_BL_DATA_WHEELSPEED").is_not_null()
)

speed = df.filter(
    pl.col("VDM_GPS_SPEED").is_not_null()
)

# writes a new parquet file
fl.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\fl.parquet")
fr.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\fr.parquet")
br.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\br.parquet")
bl.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\bl.parquet")
speed.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\speed.parquet")


# writes csvs for the parquets to make sure the data is correct
bl = pl.read_parquet("Wheel Speed Calibration/parquets/bl.parquet")
bl.select("TPERIPH_BL_DATA_WHEELSPEED").write_csv("TPERIPH_BL_DATA_WHEELSPEED")

br = pl.read_parquet("Wheel Speed Calibration/parquets/br.parquet")
br.select("TPERIPH_BR_DATA_WHEELSPEED").write_csv("TPERIPH_BR_DATA_WHEELSPEED")

fl = pl.read_parquet("Wheel Speed Calibration/parquets/fl.parquet")
fl.select("TPERIPH_FL_DATA_WHEELSPEED").write_csv("TPERIPH_FL_DATA_WHEELSPEED")

fr = pl.read_parquet("Wheel Speed Calibration/parquets/fr.parquet")
fr.select("TPERIPH_FR_DATA_WHEELSPEED").write_csv("TPERIPH_FR_DATA_WHEELSPEED")

speed = pl.read_parquet("Wheel Speed Calibration/parquets/speed.parquet")
speed.select("VDM_GPS_SPEED").write_csv("VDM_GPS_SPEED")