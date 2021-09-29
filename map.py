import folium
import pandas

volcanoes = pandas.read_csv("volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
#name = list(volcanoes["NAME"])
elev = list(volcanoes["ELEV"])

map = folium.Map(location=[39.33538223288375, -114.85099229343496], zoom_start=6, tiles="Stamen Terrain")

def elev_color(elevation):
    if elevation < 2000:
        return 'green'
    elif elevation > 3000:
        return 'red'
    else:
        return 'orange'

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, tooltip='Elevation: ' + str(el) + ' m', color = 'grey', fill_opacity = '0.7', fill_color=elev_color(el), fill=True))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'red' if x['properties']['POP2005'] > 20000000 else 'orange'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")
