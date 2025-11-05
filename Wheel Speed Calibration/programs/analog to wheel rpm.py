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
print(rpm_per_count)
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