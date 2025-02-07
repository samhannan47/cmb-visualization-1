# CMB Visualization Project

This project focuses on analyzing and visualizing the Cosmic Microwave Background (CMB) data. The CMB is the faint radiation left over from the Big Bang, and it serves as a snapshot of the universe when it was only 380,000 years old. This project allows you to load, process, and visualize the CMB data using Python.

### Setup

Follow these steps to set up and run the project on your local machine:

1. Clone the Repository
   Clone this repository to your local machine:
2. Create and Activate a Python Virtual Environment
   It's recommended to create a virtual environment to manage dependencies: `python3 -m venv cmb_env`
   and `source cmb_env/bin/activate`
3. Install Required Dependencies
   Install the required Python libraries:
4. Download the CMB Data
   Ensure you have the CMB data `COM_CMB_IQU-commander_4096_R4.00_full.fits` in the data/ directory. You can download it from Planck Legacy Archive, or you can use any other CMB dataset.

5. Run the Script
   Now, you're ready to run the Python script to load and visualize the CMB data: `python scripts/load_cmb.py`.
   This will display the temperature map of the CMB, with warm and cool regions color-coded.

### What is CMB?

The Cosmic Microwave Background (CMB) is radiation left over from the Big Bang, providing a snapshot of the universe when it was only 380,000 years old. The temperature fluctuations in the CMB carry crucial information about the early universe’s structure and composition.

This project uses HEALPix (Hierarchical Equal Area isoLatitude Pixelization) to represent the CMB data, which divides the entire sky into equal-area pixels for easier analysis and visualization.

## Next Steps

Once you have the project set up and running, here are a few directions you can explore:

### CMB Power Spectrum (Cl) Analysis:

Calculate and plot the power spectrum of the CMB, which tells us about the density fluctuations in the early universe at different angular scales.

```
power_spectrum = hp.anafast(data)
plt.loglog(np.arange(1, len(power_spectrum)), power_spectrum[1:], label="Power Spectrum")
plt.xlabel("Multipole moment (l)")
plt.ylabel("Power (Cl)")
plt.legend()
plt.show()
```

### Gaussian Smoothing:

Smooth the map to visualize large-scale features and reduce small-scale noise.

```
smoothed_map = hp.smooth(data, sigma=5.0)
hp.mollview(smoothed_map, title="Smoothed CMB Map", unit="K_CMB", cmap="coolwarm")
hp.graticule()
plt.show()
```

### Cross-correlations:

Cross-correlate the CMB data with other datasets, such as galaxy surveys or gravitational wave observations.

### Reprojection to a Cartesian Grid:

Reproject the spherical CMB data to a rectangular grid for further analysis.
