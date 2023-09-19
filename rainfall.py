# Constants
lake_area_km2 = 2  # Area of Lake Comp in square kilometers
catchment_area_km2 = 100  # Area from which rainwater is collected in square kilometers
desired_lake_depth_m = 1  # Desired increase in lake depth in meters

# Calculate the volume of water needed in cubic meters
# 1 cubic meter of water is equivalent to 1000 liters, and 1 liter is equivalent to 1 millimeter of water
volume_needed_cubic_m = lake_area_km2 * 1000000 * desired_lake_depth_m

# Calculate the amount of rain needed in millimeters
rain_needed_mm = volume_needed_cubic_m / catchment_area_km2

# Print the result with one decimal place
print(f"Rain needed to raise Lake Comp by {desired_lake_depth_m} meter(s): {rain_needed_mm:.1f} mm")

