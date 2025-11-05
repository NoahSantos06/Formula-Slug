import polars as pl


df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30.parquet")

df = df.with_columns([
    (pl.col("TPERIPH_BL_DATA_WHEELSPEED") * 0.1212).alias("TPERIPH_BL_DATA_RPM"),
    (pl.col("TPERIPH_BR_DATA_WHEELSPEED") * 0.1212).alias("TPERIPH_BR_DATA_RPM"),
    (pl.col("TPERIPH_FL_DATA_WHEELSPEED") * 0.1212).alias("TPERIPH_FL_DATA_RPM"),
    (pl.col("TPERIPH_FR_DATA_WHEELSPEED") * 0.1212).alias("TPERIPH_FR_DATA_RPM")
])

# writes a parquet to add rpm
df.write_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30_withRPM.parquet")

# writes csvs for rpm with nulls
df.select("TPERIPH_BL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back left wheel rpm.csv")
df.select("TPERIPH_BR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back right wheel rpm.csv")
df.select("TPERIPH_FL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front left wheel rpm.csv")
df.select("TPERIPH_FR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front right wheel rpm.csv")

# deletes all nulls
fl = df.filter(pl.col("TPERIPH_FL_DATA_RPM").is_not_null())
fr = df.filter(pl.col("TPERIPH_FR_DATA_RPM").is_not_null())
br = df.filter(pl.col("TPERIPH_BR_DATA_RPM").is_not_null())
bl = df.filter(pl.col("TPERIPH_BL_DATA_RPM").is_not_null())

# writes parquets for filtered data
fl.write_parquet("Wheel Speed Calibration/parquets/front left wheel rpm filtered.parquet")
fr.write_parquet("Wheel Speed Calibration/parquets/front right wheel rpm filtered.parquet")
br.write_parquet("Wheel Speed Calibration/parquets/back right wheel rpm filtered.parquet")
bl.write_parquet("Wheel Speed Calibration/parquets/back left wheel rpm filtered.parquet")

# writes csvs for filtered rpm data
bl.select("TPERIPH_BL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back left wheel rpm filtered.csv")
br.select("TPERIPH_BR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/back right wheel rpm filtered.csv")
fl.select("TPERIPH_FL_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front left wheel rpm filtered.csv")
fr.select("TPERIPH_FR_DATA_RPM").write_csv("Wheel Speed Calibration/csvs/rpm/front right wheel rpm filtered.csv")

# converts rpm to mph 
bl_mph = bl.with_columns([(pl.col("TPERIPH_BL_DATA_RPM") * 0.0476).alias("TPERIPH_BL_DATA_RPM_TO_MPH")])
br_mph = br.with_columns([(pl.col("TPERIPH_BR_DATA_RPM") * 0.0476).alias("TPERIPH_BR_DATA_RPM_TO_MPH")])
fl_mph = fl.with_columns([(pl.col("TPERIPH_FL_DATA_RPM") * 0.0476).alias("TPERIPH_FL_DATA_RPM_TO_MPH")])
fr_mph = fr.with_columns([(pl.col("TPERIPH_FR_DATA_RPM") * 0.0476).alias("TPERIPH_FR_DATA_RPM_TO_MPH")])

# writes csvs for rpm to mph conversion
bl_mph.select("TPERIPH_BL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BL_DATA_RPM_TO_MPH.csv")
br_mph.select("TPERIPH_BR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BR_DATA_RPM_TO_MPH.csv")
fl_mph.select("TPERIPH_FL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FL_DATA_RPM_TO_MPH.csv")
fr_mph.select("TPERIPH_FR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FR_DATA_RPM_TO_MPH.csv")