import os
import xlrd
import matplotlib.pyplot as plt
import matplotlib

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the Excel file
path = os.path.join(current_dir, "SpectrumAM.xls")

print(f"Attempting to open file at: {path}")

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

print(inputWorksheet.nrows)
print(inputWorksheet.ncols)

wavelength = []
AM0 = []
AM15g = []
AM15d = []

for y in range(1, inputWorksheet.nrows):
    wavelength.append(inputWorksheet.cell_value(y,0))
    AM0.append(inputWorksheet.cell_value(y,1))
    AM15g.append(inputWorksheet.cell_value(y,2))
    AM15d.append(inputWorksheet.cell_value(y,3))

matplotlib.rcParams.update({'font.size': 20})

positions = (0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000)
labels = ("0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4")
plt.xticks(positions, labels)

plt.plot(wavelength, AM0, label="AM 0")
plt.plot(wavelength, AM15g, label="AM 1.5 Global")
plt.plot(wavelength, AM15d, label="AM 1.5 Direct")
plt.axvline(x=380, c='black', linestyle='--', linewidth='2')
plt.axvline(x=740, c='black', linestyle='--', linewidth='2')

plt.xlabel("Wavelength, [\u03BCm]")
plt.ylabel("[$W/m^2/\u03BCm$]")
plt.title("Spectral Irradiance (ASTM G-173-03)")

plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
