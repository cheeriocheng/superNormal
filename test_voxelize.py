from voxlib.voxelize import voxelize
import json

voxels = [v for v in voxelize("model/chair.obj", 30)] #60

print("total voxels generated: ", len(voxels))
# print(voxels)

with open('models/chair_test.json', 'w') as outfile:
    json.dump(voxels, outfile)
