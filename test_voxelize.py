from voxlib.voxelize import voxelize


voxels = [v for v in voxelize("model/chair.obj", 10)]
print(len(voxels))
print(voxels)