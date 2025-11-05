import polars as pl

df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30_withRPM.parquet")


# filters all null values in each column
# done seperately so it doesn't mess with different columns in each parquet file

fl = df.filter(
    pl.col("TPERIPH_FL_DATA_RPM").is_not_null()
)

fr = df.filter(
    pl.col("TPERIPH_FR_DATA_RPM").is_not_null()
)

br = df.filter(
    pl.col("TPERIPH_BR_DATA_RPM").is_not_null()
)

bl = df.filter(
    pl.col("TPERIPH_BL_DATA_RPM").is_not_null()
)


bl_mph = bl.with_columns([
    (pl.col("TPERIPH_BL_DATA_RPM") * 0.00595 * 8).alias("TPERIPH_BL_DATA_RPM_TO_MPH"),
])

br_mph = br.with_columns([
    (pl.col("TPERIPH_BR_DATA_RPM") * 0.00595 * 8).alias("TPERIPH_BR_DATA_RPM_TO_MPH"),
])

fl_mph = fl.with_columns([
    (pl.col("TPERIPH_FL_DATA_RPM") * 0.00595 * 8).alias("TPERIPH_FL_DATA_RPM_TO_MPH"),
])

fr_mph = fr.with_columns([
    (pl.col("TPERIPH_FR_DATA_RPM") * 0.00595 * 8).alias("TPERIPH_FR_DATA_RPM_TO_MPH"),
])

bl_mph.select("TPERIPH_BL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BL_DATA_RPM_TO_MPH")
br_mph.select("TPERIPH_BR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BR_DATA_RPM_TO_MPH")
fl_mph.select("TPERIPH_FL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FL_DATA_RPM_TO_MPH")
fr_mph.select("TPERIPH_FR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FR_DATA_RPM_TO_MPH")
