# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:13:37 2020

@author: rlilhare
"""
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-white')

plt.subplot(1, 3, 1)
nc = NetCDFFile('ERA_Land_mn_ann_total_pcp_NRB_1981_2019.nc') # note this file is 2.5 degree, so low resolution data
nc.variables


lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time = nc.variables['time'][:]
pcp = nc.variables['pcp'][:] # avg ann pcp



map = Basemap(projection='merc',llcrnrlon=-128.,llcrnrlat=52.6,urcrnrlon=-122.3,urcrnrlat=56.4,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full


#map.drawcoastlines()
#map.drawstates()
#map.drawcountries()
map.drawlsmask(land_color='w', ocean_color='w') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)
map.readshapefile('Stuart', 'Stuart', drawbounds = True)
map.readshapefile('Middle_Nech', 'Middle_Nech', drawbounds = True)
map.readshapefile('Chilako', 'Chilako', drawbounds = True)
map.readshapefile('Lower_Nech', 'Lower_Nech', drawbounds = True)
map.readshapefile('Regulated_for_sp_plot', 'Regulated_for_sp_plot', drawbounds = True)
map.readshapefile('Nautley', 'Nautley', drawbounds = True)
# for info, shape in zip(map.Stuart_info, map.Stuart):
#     if info['Id'] == 0:
#         x, y = zip(*shape) 
#         map.plot(x, y, marker=None,color='k',linewidth=0.5)#alpha=0.1)

parallels = np.arange(50,57,2.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-128,-118,2.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],dashes=[4,500], color='k',fontsize=6)
map.drawmeridians(meridians,labels=[0,0,0,1], dashes=[4,500], color='k',fontsize=6) #meridians,labels=[0,0,0,1],fontsize=6)



lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)


temp = map.contourf(x,y,pcp[0,:,:],range(100, 2500,200), cmap='RdYlGn')
cb = map.colorbar(temp,"bottom", size="4%", pad="8%") #pad takes label down
#cb = plt.colorbar(temp) #pad takes label down
#plt.clim(450, 2400)

plt.title('(a) Precipitation',fontsize=10)
cb.set_label('(mm)',fontsize=6)

clevs1 =np.arange(100,2500,200) #clevs1 =np.arange(479,2396,200)
font_size = 6 # Adjust as appropriate.

cb.ax.tick_params(labelsize=font_size)
#cb.ax.set_xticklabels(clevs1[::1],rotation=45)

#cb.set_ticks(np.linspace(0, 2500))
#cb.set_ticklabels(range(2500))
#cb.colorbar(extend='both')
#plt.clim(-1, 1);



plt.subplot(1, 3, 2)
nc = NetCDFFile('ERA_Land_mn_ann_total_snowfall_NRB_1981_2019.nc') # note this file is 2.5 degree, so low resolution data
nc.variables


lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time = nc.variables['time'][:]
sf = nc.variables['sf_mm'][:] # avg ann pcp






map = Basemap(projection='merc',llcrnrlon=-128.,llcrnrlat=52.6,urcrnrlon=-122.3,urcrnrlat=56.4,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full


#map.drawcoastlines()
#map.drawstates()
#map.drawcountries()
map.drawlsmask(land_color='w', ocean_color='w') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)


parallels = np.arange(50,57,2.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-128,-118,2.) # make longitude lines every 5 degrees from 95W to 70W
#map.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
map.drawmeridians(meridians,labels=[0,0,0,1], dashes=[4,500], color='k',fontsize=6)



lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)


temp1 = map.contourf(x,y,sf[0,:,:],range(100, 2500,200),cmap='RdYlGn')
cb = map.colorbar(temp1,"bottom", size="4%", pad="8%", extend="both") #pad takes label down

plt.title('(b) Snowfall',fontsize=10)
cb.set_label('(mm)',fontsize=6)
clevs1 =np.arange(100,2500,200)
font_size = 6 # Adjust as appropriate.

cb.ax.tick_params(labelsize=font_size)
#cb.ax.set_xticklabels(clevs1[::1],rotation=45)
#cb.set_ticks(np.linspace(0, 2500))
#cb.set_ticklabels(range(2500))
#cb.colorbar(extend='both')
#plt.clim(-1, 1);


plt.subplot(1, 3, 3)
nc = NetCDFFile('ERA_Land_mn_ann_total_rainf_NRB_1981_2019.nc') # note this file is 2.5 degree, so low resolution data
nc.variables


lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time = nc.variables['time'][:]
rainf = nc.variables['snowf'][:] # avg ann pcp



map = Basemap(projection='merc',llcrnrlon=-128.,llcrnrlat=52.6,urcrnrlon=-122.3,urcrnrlat=56.4,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full


#map.drawcoastlines()
#map.drawstates()
#map.drawcountries()
map.drawlsmask(land_color='w', ocean_color='w') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)


parallels = np.arange(50,57,2.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-128,-118,2.) # make longitude lines every 5 degrees from 95W to 70W
#map.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
map.drawmeridians(meridians,labels=[0,0,0,1], dashes=[4,500], color='k',fontsize=6)



lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)


temp2 = map.contourf(x,y,rainf[0,:,:],range(100, 2500,200),cmap='RdYlGn')
cb = map.colorbar(temp2,"bottom", size="4%", pad="8%", extend="both") #pad takes label down

plt.title('(c) Rainfall',fontsize=10)
cb.set_label('(mm)',fontsize=6)
clevs1 =np.arange(100,2500,200) #clevs1 =np.arange(479,2396,200)
font_size = 6 # Adjust as appropriate.

cb.ax.tick_params(labelsize=font_size)
#cb.ax.set_xticklabels(clevs1[::1],rotation=45)
#cb.set_ticks(np.linspace(0, 2500))
#cb.set_ticklabels(range(2500))
#cb.colorbar(extend='both')
#plt.clim(-1, 1);



plt.savefig('NRB_spatial_avg_ann_pcp.png', format='png', dpi=300)





