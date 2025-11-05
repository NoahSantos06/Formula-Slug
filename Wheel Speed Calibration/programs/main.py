import polars as pl
import numpy as np

pi = np.pi
R_w = 8 # radius of wheel in inches
T = 60 # number of teeth per revolution
V_cc = 3.3 # fixed supply voltage powering the LM2907
V_max = 51.61 / 3600 # max velocity recorded 
k = 1 # gain constant typically 1
I2 = 0.00018 # varies 140 - 240 uA
V_Omax = 5 # maximum output voltage (0 -> 5V)
V_ref = 5 # maximum input voltage that the ADC can convert into its maximum digital value (0 -> 5) -> (0 - 32767)

v_max = (63360 * V_max * T) / (2 * pi * R_w) # maximum input frequency
C1 = I2 / (v_max * V_cc) # timing capicitator
R1 = V_Omax / I2 # resistor that sets output voltage scale of LM2907. Controls how much output voltage we get per hertz of input frequency

# V_o = otuput voltage that is then converted into the unsigned 16 bit integer
# count = (60 * V_ref) / (32767)    to convert from analog voltage to count 
# RPM = V_o / (V_cc * f_in * C1 * R1 * k)

rpm_per_count = (60 * V_ref) / (32767 * V_cc * R1 * C1 * k * T)
# rpm_per_count = 0.18356
mph_per_rpm = 0.0476
# mph_per_rpm = mph_per_rpm

df = pl.read_parquet("Wheel Speed Calibration/parquets/firstDriveMCError30.parquet")

df = df.with_columns([
    (pl.col("TPERIPH_BL_DATA_WHEELSPEED") * rpm_per_count).alias("TPERIPH_BL_DATA_RPM"),
    (pl.col("TPERIPH_BR_DATA_WHEELSPEED") * rpm_per_count).alias("TPERIPH_BR_DATA_RPM"),
    (pl.col("TPERIPH_FL_DATA_WHEELSPEED") * rpm_per_count).alias("TPERIPH_FL_DATA_RPM"),
    (pl.col("TPERIPH_FR_DATA_WHEELSPEED") * rpm_per_count).alias("TPERIPH_FR_DATA_RPM")
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
bl_mph = bl.with_columns([(pl.col("TPERIPH_BL_DATA_RPM") * mph_per_rpm).alias("TPERIPH_BL_DATA_RPM_TO_MPH")])
br_mph = br.with_columns([(pl.col("TPERIPH_BR_DATA_RPM") * mph_per_rpm).alias("TPERIPH_BR_DATA_RPM_TO_MPH")])
fl_mph = fl.with_columns([(pl.col("TPERIPH_FL_DATA_RPM") * mph_per_rpm).alias("TPERIPH_FL_DATA_RPM_TO_MPH")])
fr_mph = fr.with_columns([(pl.col("TPERIPH_FR_DATA_RPM") * mph_per_rpm).alias("TPERIPH_FR_DATA_RPM_TO_MPH")])

# writes csvs for rpm to mph conversion

bl_mph.write_parquet("Wheel Speed Calibration/parquets/TPERIPH_BL_DATA_RPM_TO_MPH.parquet")
br_mph.write_parquet("Wheel Speed Calibration/parquets/TPERIPH_BR_DATA_RPM_TO_MPH.parquet")
fl_mph.write_parquet("Wheel Speed Calibration/parquets/TPERIPH_FL_DATA_RPM_TO_MPH.parquet")
fr_mph.write_parquet("Wheel Speed Calibration/parquets/TPERIPH_FR_DATA_RPM_TO_MPH.parquet")

bl_mph.select("TPERIPH_BL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BL_DATA_RPM_TO_MPH.csv")
br_mph.select("TPERIPH_BR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_BR_DATA_RPM_TO_MPH.csv")
fl_mph.select("TPERIPH_FL_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FL_DATA_RPM_TO_MPH.csv")
fr_mph.select("TPERIPH_FR_DATA_RPM_TO_MPH").write_csv("Wheel Speed Calibration/csvs/rpm to mph/TPERIPH_FR_DATA_RPM_TO_MPH.csv")