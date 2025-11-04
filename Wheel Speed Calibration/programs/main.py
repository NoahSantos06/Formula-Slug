import polars as pl

df = pl.read_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\firstDriveMCError30.parquet")

# wheel speed to rpm conversion for the parquet
df = df.with_columns([
    (pl.col("TPERIPH_BL_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_BL_DATA_RPM"),
    (pl.col("TPERIPH_BR_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_BR_DATA_RPM"),
    (pl.col("TPERIPH_FL_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_FL_DATA_RPM"),
    (pl.col("TPERIPH_FR_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_FR_DATA_RPM")
])

df.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\firstDriveMCError30_withRPM.parquet")


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

