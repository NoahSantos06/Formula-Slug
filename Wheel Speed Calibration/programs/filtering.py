import polars as pl

p1 = pl.read_parquet("Wheel Speed Calibration/parquets/1108-11_54.parquet")
p1 = p1.with_columns(pl.all().fill_null(strategy="forward")).with_columns(pl.all().fill_null(strategy="backward"))
p1.write_parquet("Wheel Speed Calibration/parquets/1108-11_54_filtered.parquet")

p2 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_26.parquet")
p2 = p2.with_columns(pl.all().fill_null(strategy="forward")).with_columns(pl.all().fill_null(strategy="backward"))
p2.write_parquet("Wheel Speed Calibration/parquets/1109-4_26_filtered.parquet")

p3 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_30.parquet")
p3 = p3.with_columns(pl.all().fill_null(strategy="forward")).with_columns(pl.all().fill_null(strategy="backward"))
p3.write_parquet("Wheel Speed Calibration/parquets/1109-4_30_filtered.parquet")

p4 = pl.read_parquet("Wheel Speed Calibration/parquets/1109-4_53.parquet")
p4 = p4.with_columns(pl.all().fill_null(strategy="forward")).with_columns(pl.all().fill_null(strategy="backward"))
p4.write_parquet("Wheel Speed Calibration/parquets/1109-4_53_filtered.parquet")
