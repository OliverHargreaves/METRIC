import arcpy

# Data
EC="C:/Users/graduate/Box/DiviningWater/METRIC/Modena shapefiles/EC_Tower/EC_Tower.shp"
P4="C:/Users/graduate/Box/DiviningWater/METRIC/Modena shapefiles/Pivot_4_Boundary/Pivot_4_Boundary.shp"
P22="C:/Users/graduate/Box/DiviningWater/METRIC/Modena shapefiles/Pivot_22_Boundary/Pivot_22_Boundary.shp"
P30="C:/Users/graduate/Box/DiviningWater/METRIC/Modena shapefiles/Pivot_30_Boundary/Pivot_30_Boundary.shp"

ET="et24_ef_20211028_P39R34_L8.img"

# Create output folder
arcpy.CreateFolder_management(out_folder_path="C:/Users/graduate/Box/DiviningWater/METRIC/2021/20211028", out_name="Outputs")

# Clip ET raster to polygons
ET_EC=arcpy.Clip_management(in_raster = ET, 
                            rectangle = "#", 
                            out_raster = "/Outputs/ET_EC.img", 
                            in_template_dataset = EC, 
                            nodata_value = 666,
                            clipping_geometry = 'ClippingGeometry', 
                            maintain_clipping_extent = 'NO_MAINTAIN_EXTENT')

ET_P4=arcpy.Clip_management(in_raster = ET, 
                            rectangle = "#", 
                            out_raster = "Outputs/ET_P4.img", 
                            in_template_dataset = P4, 
                            nodata_value = 666,
                            clipping_geometry = 'ClippingGeometry', 
                            maintain_clipping_extent = 'NO_MAINTAIN_EXTENT')

ET_P22=arcpy.Clip_management(in_raster = ET, 
                            rectangle = "#", 
                            out_raster = "Outputs/ET_P22.img", 
                            in_template_dataset = P22, 
                            nodata_value = 666,
                            clipping_geometry = 'ClippingGeometry', 
                            maintain_clipping_extent = 'NO_MAINTAIN_EXTENT')

ET_P30=arcpy.Clip_management(in_raster = ET, 
                            rectangle = "#", 
                            out_raster = "Outputs/ET_P30.img", 
                            in_template_dataset = P30, 
                            nodata_value = 666,
                            clipping_geometry = 'ClippingGeometry', 
                            maintain_clipping_extent = 'NO_MAINTAIN_EXTENT')

# Get stats
EC_mean=arcpy.GetRasterProperties_management("Outputs/ET_EC.img", "MEAN")
EC_std=arcpy.GetRasterProperties_management("Outputs/ET_EC.img", "STD")

P4_mean=arcpy.GetRasterProperties_management("Outputs/ET_P4.img", "MEAN")
P4_std=arcpy.GetRasterProperties_management("Outputs/ET_P4.img", "STD")

P22_mean=arcpy.GetRasterProperties_management("Outputs/ET_P22.img", "MEAN")
P22_std=arcpy.GetRasterProperties_management("Outputs/ET_P22.img", "STD")

P30_mean=arcpy.GetRasterProperties_management("Outputs/ET_P30.img", "MEAN")
P30_std=arcpy.GetRasterProperties_management("Outputs/ET_P30.img", "STD")

# print results
print(EC_mean)
print(EC_std)
print(P4_mean)
print(P4_std)
print(P22_mean)
print(P22_std)
print(P30_mean)
print(P30_std)

