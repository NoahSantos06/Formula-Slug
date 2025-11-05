import polars as pl

df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30_withRPM.parquet")

bl_rpm = df.filter(pl.col('TPERIPH_BL_DATA_RPM').is_not_null())
br_rpm = df.filter(pl.col('TPERIPH_BR_DATA_RPM').is_not_null())
fl_rpm = df.filter(pl.col('TPERIPH_FL_DATA_RPM').is_not_null())
fr_rpm = df.filter(pl.col('TPERIPH_FR_DATA_RPM').is_not_null())



