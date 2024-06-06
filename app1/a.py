# import time

# while True:
#     with open("Total amount.txt","r") as f:
#         data = f.read()
#         if data:
#             print("hello")
#             time.sleep(1)
#         else:
#             with open("Total amount.txt","w") as f:
#                 data = f.write("q")
#             break
            
from landsatxplore.api import API

# Your USGS  credentials
username = "HIMANI@"
password = "Himani#03210"

# Initialize a new API instance
api = API(username, password)
scenes = api.search(
    dataset='landsat_ot_c2_l2',
    latitude=53.36305556,
    longitude=-6.15583333,
    start_date='2023-01-18',
    end_date='2023-12-31',
    max_cloud_cover=50
)
# Perform a request
response = api.request(endpoint="dataset-catalogs")
# print(scenes)

from landsatxplore.earthexplorer import EarthExplorer
import os

# Initialize the API
ee = EarthExplorer(username, password)

# # Select the first scene
ID = 'LC09_L2SP_015019_20240207_20240209_02_T2'

# # Download the scene 
# try: 
#     ee.download(ID, output_dir='./data')
#     print('{} succesful'.format(ID))
    
# # Additional error handling
# except:
#     if os.path.isfile('./data/{}.tif'.format(ID)):
#         print('{} error but file exists'.format(ID))
#     else:
#         print('{} error'.format(ID))

# ee.logout()

# import tarfile

# # Extract files from tar archive
# tar = tarfile.open('./data/{}.tar'.format(ID))
# tar.extractall('./data/{}'.format(ID))
# tar.close()


# import tifffile as tiff
# import numpy as np
# import matplotlib.pyplot as plt

# # Load Blue (B2), Green (B3) and Red (B4) bands
# B2 = tiff.imread('./data/{}/{}_SR_B2.TIF'.format(ID, ID))
# B3 = tiff.imread('./data/{}/{}_SR_B3.TIF'.format(ID, ID))
# B4 = tiff.imread('./data/{}/{}_SR_B4.TIF'.format(ID, ID))

# # Stack and scale bands
# RGB = np.dstack((B4, B3, B2))
# RGB = np.clip(RGB*0.0000275-0.2, 0, 1)

# # Clip to enhance contrast
# RGB = np.clip(RGB,0,0.2)/0.2

# # Display RGB image
# fig, ax = plt.subplots(figsize=(10, 10))
# plt.show(RGB)
# # ax.set_axis_off()

# import rasterio
# from rasterio.windows import Window
# import numpy as np

# def calculate_ndwi(nir_band, green_band):
#     # Ensure the bands have the same shape
#     assert nir_band.shape == green_band.shape, "Band shapes do not match"
    
#     # Calculate NDWI
#     ndwi = (green_band - nir_band) / (green_band + nir_band + 1e-9)  # Add a small value to avoid division by zero
    
#     return ndwi

# # Open NIR and Green bands
# with rasterio.open('C:\\Users\\pradeepwebdev\\Desktop\\IOT\\IOT_dashboard\\data\\LC09_L2SP_015019_20240207_20240209_02_T2\\LC09_L2SP_015019_20240207_20240209_02_T2_SR_B1.tif') as src:
#     nir_band = src.read(3)  # Assuming NIR band is band 3
#     green_band = src.read(3)  # Assuming Green band is band 2
#     profile = src.profile

# # Calculate NDWI
# ndwi = calculate_ndwi(nir_band, green_band)

# # Write NDWI to a new TIFF file
# with rasterio.open('ndwi.tif', 'w', **profile) as dst:
#     dst.write(ndwi, 1)  # Write NDWI to band 1

# print("NDWI calculation completed and saved to ndwi.tif")


# Import necessary QGIS modules
from pytest_qgis.utils import QgsApplication, QgsRasterLayer, QgsRasterCalculator, QgsCoordinateReferenceSystem

# Start a QGIS application
qgs = QgsApplication([], False)
qgs.initQgis()

# Define paths to input and output files
input_tiff_path = '/path/to/your/input/landsat8_image.tif'
output_ndwi_path = '/path/to/your/output/ndwi.tif'

# Load the Landsat 8 TIFF file into QGIS
layer = QgsRasterLayer(input_tiff_path, 'Landsat 8 Image')
if not layer.isValid():
    print('Error: Unable to load input TIFF file.')
else:
    # Define NDWI expression
    ndwi_expression = '(B3 - B5) / (B3 + B5)'

    # Set up raster calculator
    raster_calc = QgsRasterCalculator(ndwi_expression, output_ndwi_path, 'GTiff', layer.extent(), layer.width(), layer.height(), layer.crs(), layer.renderer().dataType(), layer.renderer().source())
    
    # Perform the calculation
    result = raster_calc.processCalculation()
    
    # Check for errors
    if result == QgsRasterCalculator.NoError:
        print('NDWI calculation successful. Output saved to:', output_ndwi_path)
    else:
        print('Error occurred during NDWI calculation.')

# Exit the QGIS application
qgs.exitQgis()

