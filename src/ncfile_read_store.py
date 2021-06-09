import os

from netCDF4 import Dataset as NetCDFFile


def read_nc_data():
    base_path = os.getcwd()
    pcp_path = os.path.join(
        base_path, "./data/ERA_Land_mn_ann_total_pcp_NRB_1981_2019.nc"
    )
    sf_path = os.path.join(
        base_path, "./data/ERA_Land_mn_ann_total_snowfall_NRB_1981_2019.nc"
    )
    rain_path = os.path.join(
        base_path, "./data/ERA_Land_mn_ann_total_rainf_NRB_1981_2019.nc"
    )
    nc = NetCDFFile(pcp_path)  # Input your file in a netcdf format
    nc1 = NetCDFFile(sf_path)  # Input your file in a netcdf format
    nc2 = NetCDFFile(rain_path)  # Input your file in a netcdf format
    lat = nc.variables["lat"][:]
    lon = nc.variables["lon"][:]
    # Plotting variable in the plot (avg ann air temp)
    pcp = nc.variables["pcp"][:]
    sf_mm = nc1.variables["sf_mm"][:]
    rain = nc2.variables["snowf"][:]
    return lat, lon, pcp, sf_mm, rain
