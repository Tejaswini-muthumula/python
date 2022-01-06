import folium
from folium.map import LayerControl
import pandas

data = pandas.read_csv("Volcanoes.txt")


lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return"green"
    elif 1000< elevation < 3000:
        return "red"
    else:
        return "pink"
map= folium.Map(location= [36.8,-99.09],zoom_start=6, title ="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volacanoes")

for ln,lo,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[ln,lo], popup=str(el), fill_color =color_producer(el),color = "grey",fill_opacity =0.75))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor' : "green" if x['properties']['POP2005']< 10000000 
else "orange" if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")