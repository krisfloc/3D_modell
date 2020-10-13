from laspy.file import File
import numpy as np
import open3d as o3d

# load file
inFile = File("Data18.las", mode="r")

coords = np.vstack((inFile.x, inFile.y, inFile.z)).transpose()

avg = 0
for z in inFile.z:
    avg += int(round(z))
avg = avg / len(inFile.z)

mid = (min(inFile.x) + max(inFile.x)) / 2

temp = []
for z in coords:
    if z[2] > avg+5:
        temp.append(z)
coords = np.asarray(temp)

temp = []
for x in coords:
    if x[0] < mid:
        temp.append(x)
coords = np.asarray(temp)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(coords)
o3d.io.write_point_cloud("data18.ply", pcd)

pcd = o3d.io.read_point_cloud("data18.ply")
o3d.visualization.draw_geometries([pcd])
