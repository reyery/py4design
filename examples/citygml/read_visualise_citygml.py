import time
import pylibudo

#================================================================================
#INSTRUCTION: SPECIFY THE CITYGML FILE
#================================================================================
citygml_filepath = "F:\\kianwee_work\\smart\\conference\\asim2016\\asim_example\\citygml\\punggol_citygml_asim.gml"
citygml_filepath = "F:\\kianwee_work\\smart\\conference\\asim2016\\asim_example\\citygml\\punggol_citygml_asim_origlvl.gml"
#================================================================================
#INSTRUCTION: SPECIFY THE CITYGML FILE
#================================================================================


time1 = time.clock()
display_2dlist = []
#===================================================================================================
#read the citygml file 
#===================================================================================================
read_citygml = pylibudo.pycitygml.Reader(citygml_filepath)
buildings = read_citygml.get_buildings()
landuses = read_citygml.get_landuses()
stops = read_citygml.get_bus_stops()
roads = read_citygml.get_roads()
railways = read_citygml.get_railways()

print "nbuildings:", len(buildings)

#get all the polylines of the lod0 roads
for road in roads:
    polylines = read_citygml.get_linestring(road)

#get all the polygons of the landuses
for landuse in landuses:
    polygons = read_citygml.get_polygons(landuse)
    
#get all the stations in the buildings and extract their polygons 
stations = []
for building in buildings:
    bclass = building.find("bldg:class", namespaces=read_citygml.namespaces).text
    bfunction = building.find("bldg:function", namespaces=read_citygml.namespaces).text
    
    if bclass == "1170" and bfunction == "2480":
        stations.append(building)
    polygons = read_citygml.get_polygons(building)
    for polygon in polygons:
        polygon_id = polygon.attrib["{%s}id" % read_citygml.namespaces['gml']]
        pos_list = read_citygml.get_poslist(polygon)
        
bdisplay_list = []
#extract all the footprint of the buildings 
building_footprints = []
for building in buildings:
    pypolgon_list = read_citygml.get_pypolygon_list(building)
    solid = pylibudo.threedmodel.pypolygons2occsolid(pypolgon_list)
    bdisplay_list.append(solid)

    
#find all the buildings inside the landuse 
ldisplay_list = []

for landuse in landuses:
    lpolygons = read_citygml.get_polygons(landuse)
    if lpolygons:
        lpolygon = read_citygml.get_polygons(landuse)[0]
        landuse_pts = read_citygml.polygon_2_pt_list(lpolygon)
        lface = pylibudo.py3dmodel.construct.make_polygon(landuse_pts)
        ldisplay_list.append(lface)
    
time2 = time.clock()   
time = (time2-time1)/60.0
print "TIME TAKEN", time
print "VISUALISING"  

display_2dlist.append(ldisplay_list)
display_2dlist.append(bdisplay_list)
colour_list = ["WHITE", "WHITE"]
pylibudo.py3dmodel.construct.visualise(display_2dlist, colour_list)