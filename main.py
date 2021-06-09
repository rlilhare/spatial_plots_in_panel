from src.ncfile_read_store import read_nc_data
from src.plot_data import plot_data
from src.shapefile_read_store import read_shp_file


def main():
    lat, lon, pcp, sf_mm, rain = read_nc_data()
    map = read_shp_file()
    plot_data(lat, lon, pcp, sf_mm, rain, map)


if __name__ == "__main__":
    main()
