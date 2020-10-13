from RANSAC import *

pcd = o3d.io.read_point_cloud("data18.ply")
o3d.visualization.draw_geometries([pcd])
