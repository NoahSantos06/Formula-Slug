import polars as pl

df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30.parquet")

df = df.with_columns([
    (pl.col("TPERIPH_BL_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_BL_DATA_RPM"),
    (pl.col("TPERIPH_BR_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_BR_DATA_RPM"),
    (pl.col("TPERIPH_FL_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_FL_DATA_RPM"),
    (pl.col("TPERIPH_FR_DATA_WHEELSPEED") * 0.00202).alias("TPERIPH_FR_DATA_RPM")
])

df.write_parquet(r"C:\Users\noahs\.vscode\formula slug\Wheel Speed Calibration\parquets\firstDriveMCError30_withRPM.parquet")

