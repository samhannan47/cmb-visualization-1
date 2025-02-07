import healpy as hp
import astropy.io.fits as fits
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    # Load the FITS file
    filename = "./data/COM_CMB_IQU-commander_4096_R4.00_full.fits"
    
    try:
        with fits.open(filename) as hdulist:
            # Extract CMB temperature data (1st column of 2nd HDU)
            data = hdulist[1].data["TEMPERATURE"].flatten()

            # Compute HEALPix nside
            num_pixels = len(data)
            nside = 512

            print(f"Using nside = {nside}, HEALPix pixels = {num_pixels}")

            # Apply smoothing to the data
            print("Smoothing the data...")
            start_time = time.time()
            smoothed_data = hp.smoothing(data, fwhm=np.radians(.1))
            end_time = time.time()
            print(f"Data smoothed in {end_time - start_time:.2f} seconds.")

            # Plot the CMB map
            hp.mollview(smoothed_data, title="Smoothed CMB Temperature Map", unit="K_CMB", cmap="coolwarm")
            hp.graticule()

            # Show the plot
            plt.show()

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except OSError as e:
        print(f"Error opening FITS file: {e}")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()