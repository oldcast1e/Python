import folium
import webbrowser

pos = [37.55,127.075]
map = folium.Map(pos,zoom_start=15)

folium.Marker(pos,"Sejong Unoversity",
        icon=folium.Icon(icon='cloud')).add_to(map)
file_html = "c:￦￦test￦m.html"
map.save(file_html)
webbrowser.open(file_html)