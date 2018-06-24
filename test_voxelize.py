from voxlib.voxelize import voxelize
import json

filename = "chair1"
voxels = [v for v in voxelize("models_unprocessed/{}.obj".format(filename), 30)] #60

print("Total voxels generated: ", len(voxels))
# print(voxels)

with open('models/{}.json'.format(filename), 'w') as outfile:
    json.dump(voxels, outfile)
