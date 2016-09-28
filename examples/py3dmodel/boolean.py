import pyliburo

points1 = [(50,100,0), (75,75,0), (75,60,0),(100,60,0),(100,50,0), (50,0,0),(0,50,0)]#clockwise
points2 = [(60,50,0), (50,75,0),(40,50,0),(50,40,0)]#counterclockwise
points3 = [(75,100,0), (100,100,0),(100,150,0),(75,150,0)]
face1 = pyliburo.py3dmodel.construct.make_polygon(points1)
face2 = pyliburo.py3dmodel.construct.make_polygon(points2)

res = pyliburo.py3dmodel.fetch.shape2shapetype(pyliburo.py3dmodel.construct.boolean_common(face1,face2))
res2 =pyliburo.py3dmodel.fetch.shape2shapetype(pyliburo.py3dmodel.construct.boolean_difference(face1,face2))

face = pyliburo.py3dmodel.fetch.geom_explorer(res2, "face")[0]
pts = pyliburo.py3dmodel.fetch.pyptlist_frm_occface(face)
wires = pyliburo.py3dmodel.fetch.wires_frm_face(face)

print pts
print len(wires)
#print pyliburo.py3dmodel.fetch.is_compound_null(res2)

display2dlist = []
display2dlist.append([res2])
pyliburo.py3dmodel.construct.visualise(display2dlist, ["WHITE"])