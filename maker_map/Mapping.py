import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
#df = pandas.DataFrame(data)
#print(df)
#df1= df.iloc[:,-2:]
#print(df1)

#print(data)
lat = list(data["LAT"])
lon = list(data["LON"])

map= folium.Map(location= [36.8,-99.09],zoom_start=6, title ="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")

for ln,lo in zip(lat,lon):
    fg.add_child(folium.Marker(location=[ln,lo], popup="Hi I'm a marker", icon= folium.Icon(color ="red")))
map.add_child(fg)
map.save("Map1.html")