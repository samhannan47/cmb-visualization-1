import healpy as hp
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt

# Load the FITS file
filename = "../data/COM_CMB_IQU-commander_4096_R4.00_full.fits"
hdulist = fits.open(filename)

# Extract CMB temperature data (1st column of 2nd HDU)
data = hdulist[1].data["TEMPERATURE"].flatten()

# Compute HEALPix nside
num_pixels = len(data)
nside = int(np.sqrt(num_pixels / 12))

print(f"Using nside = {nside}, HEALPix pixels = {num_pixels}")

# Plot the CMB map
hp.mollview(data, title="CMB Temperature Map", unit="K_CMB", cmap="coolwarm")
hp.graticule()

# Show the plot
plt.show()

hdulist.close()
