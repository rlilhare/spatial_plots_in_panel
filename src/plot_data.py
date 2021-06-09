import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-white")


def plot_data(lat, lon, pcp, sf_mm, rain, map):
    plt.subplot(1, 3, 1)
    parallels = np.arange(
        50, 57, 2.0
    )  # make latitude lines ever 5 degrees from 30N-50N
    meridians = np.arange(
        -128, -118, 2.0
    )  # make longitude lines every 5 degrees from 95W to 70W
    map.drawparallels(
        parallels, labels=[1, 0, 0, 0], dashes=[4, 500], color="k", fontsize=6
    )
    map.drawmeridians(
        meridians, labels=[0, 0, 0, 1], dashes=[4, 500], color="k", fontsize=6
    )  # meridians,labels=[0,0,0,1],fontsize=6)

    lons, lats = np.meshgrid(
        lon, lat
    )  # for this dataset, lon is 0 to 360, subtract 180 to display on the map
    x, y = map(lons, lats)
    pcp = map.contourf(x,y,pcp[0,:,:],range(100, 2500,200), cmap='RdYlGn')
    # pad takes label down
    cb = map.colorbar(pcp, "bottom", size="4%", pad="8%")

    plt.title('(a) Precipitation',fontsize=10)
    cb.set_label('(mm)',fontsize=6)

    font_size = 6  # Adjust as appropriate.

    cb.ax.tick_params(labelsize=font_size)  # define label font size
###################################################
    plt.subplot(1, 3, 2)
    parallels = np.arange(
        50, 57, 2.0
    )  # make latitude lines ever 5 degrees from 30N-50N
    meridians = np.arange(
        -128, -118, 2.0
    )  # make longitude lines every 5 degrees from 95W to 70W
    map.drawparallels(
        parallels, labels=[1, 0, 0, 0], dashes=[4, 500], color="k", fontsize=6
    )
    map.drawmeridians(
        meridians, labels=[0, 0, 0, 1], dashes=[4, 500], color="k", fontsize=6
    )  # meridians,labels=[0,0,0,1],fontsize=6)

    lons, lats = np.meshgrid(
        lon, lat
    )  # for this dataset, lon is 0 to 360, subtract 180 to display on the map
    x, y = map(lons, lats)
    sf_mm = map.contourf(x,y,sf_mm[0,:,:],range(100, 2500,200),cmap='RdYlGn')
    cb = map.colorbar(sf_mm,"bottom", size="4%", pad="8%", extend="both") #pad takes label down

    plt.title('(b) Snowfall',fontsize=10)
    cb.set_label('(mm)',fontsize=6)
    font_size = 6 # Adjust as appropriate.

    cb.ax.tick_params(labelsize=font_size)
##################################################
    plt.subplot(1, 3, 3)
    parallels = np.arange(
        50, 57, 2.0
    )  # make latitude lines ever 5 degrees from 30N-50N
    meridians = np.arange(
        -128, -118, 2.0
    )  # make longitude lines every 5 degrees from 95W to 70W
    map.drawparallels(
        parallels, labels=[1, 0, 0, 0], dashes=[4, 500], color="k", fontsize=6
    )
    map.drawmeridians(
        meridians, labels=[0, 0, 0, 1], dashes=[4, 500], color="k", fontsize=6
    )  # meridians,labels=[0,0,0,1],fontsize=6)

    lons, lats = np.meshgrid(
        lon, lat
    )  # for this dataset, lon is 0 to 360, subtract 180 to display on the map
    x, y = map(lons, lats)
    rain = map.contourf(x,y,rain[0,:,:],range(100, 2500,200),cmap='RdYlGn')
    cb = map.colorbar(rain,"bottom", size="4%", pad="8%", extend="both") #pad takes label down

    plt.title('(c) Rainfall',fontsize=10)
    cb.set_label('(mm)',fontsize=6)
    font_size = 6 # Adjust as appropriate.

    cb.ax.tick_params(labelsize=font_size)

    plt.savefig('NRB_spatial_avg_ann_pcp.png', format='png', dpi=300)


