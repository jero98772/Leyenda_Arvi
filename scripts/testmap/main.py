def writetxt(name,content,mode="w"):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, mode) as file:
    file.write(content)
    file.close()
import random

def generate_random_coordinates():
    # Generate a random latitude between -90 and 90 degrees
    latitude = random.uniform(-90, 90)
    
    # Generate a random longitude between -180 and 180 degrees
    longitude = random.uniform(-180, 180)
    
    return latitude, longitude
def genMap(data,name):
  import folium

  m = folium.Map(location=[0, 0])
  #folium.TileLayer('Mapbox Control Room').add_to(m)
  for i in range(10):
    lat,lon = generate_random_coordinates()
    popup="<a href='hola.com'>hola</a>"#data["name"][i]+"<li>"+data["contact"][i]+"</li><br>"
    folium.Marker([str(lat),str(lon)], popup=popup).add_to(m)
  m.save(name)
def nullValue(val,newval="-"):
    if not val or val=="":
        return newval 
#genMap(0,"test")
import pydeck as pdk
import pandas as pd
class configMap:
    """
    class for draw in map
    """
    def __init__(self,data):

        self.emptyMap = pdk.Layer(
            type="PathLayer",
            data="",
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path="edges",
            get_width=1,
        )

        self.pathMap = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=True,
            get_color=(0,155,0),
            width_scale=1,
            width_min_pixels=1,
            get_path=["lng","lat"],
            get_width=2,
        )

        self.nodesMap = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=["lng","lat"],
            get_radius=1,
            get_fill_color=[137, 36, 250],
            get_line_color=[0, 0, 0],
        )

    def newPath(data,tag="path",color=(0,15,205)):
        newPath = pdk.Layer(
            type="PathLayer",
            data=data,
            pickable=False,
            get_color=color,
            width_scale=5,
            width_min_pixels=5,
            get_path=["lng","lat"],
            get_width=5,
        )
        return newPath

    def genMapMultlayer(self,fileName,layers:list):
        view = pdk.ViewState(latitude=6.268881044071327, longitude= -75.49672372106615, pitch=40, zoom=16)
        mapCompleate = pdk.Deck(layers=layers, initial_view_state=view)
        mapCompleate.to_html(fileName)
    
    def getEmptyMap(self):return self.emptyMap
    def getPathMap(self):return self.pathMap
    def getnodesMap(self):return self.nodesMap
data=[]
columns=["lng","lat"]
for i in range(10):
    d1,d2=generate_random_coordinates()
    data.append([d1,d2])
my_points=[[-75.4951161823077,6.265695702561827],[-75.49672372106615,6.268881044071327],[-75.49431480119169,6.266710674021357],[-75.4965374219183,6.266563029351161],[-75.49412205704012,6.268923631330613],[-75.49535631183988,6.267000603026892]]

print(data,my_points)
df=pd.DataFrame(my_points, columns=columns)
datap1={"path":[[[-75.4951161823077,6.265695702561827],[-75.49672372106615,6.268881044071327],[-75.49431480119169,6.266710674021357],[-75.4965374219183,6.266563029351161],[-75.49412205704012,6.268923631330613],[-75.4951161823077,6.265695702561827]]]}
print(datap1)
dfpath1=pd.DataFrame(datap1,columns=["path"])
print(dfpath1)

a=configMap(df)
layer = pdk.Layer(
    'ScatterplotLayer',
    df,
    radius_scale=6,
    opacity=0.8,
    stroked=True,
    filled=True,
    get_position=['lng','lat'],
    auto_highlight=True,
    get_radius=1,
    radius_min_pixels=1,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_fill_color=[137, 36, 250],
    get_line_color=[0, 0, 0],
    pickable=True)

newPath = pdk.Layer(
    "PathLayer",
    dfpath1,
    pickable=False,
    get_color=(0,155,0),
    width_scale=5,
    opacity=0.8,
    stroked=True,
    filled=True,
    get_path="path",
    width_min_pixels=5,
    get_width=2
)
#b=a.getnodesMap()#a.getEmptyMap()
#c=a.newPath()
a.genMapMultlayer("points5.html",[layer,newPath])