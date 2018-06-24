import argparse
from voxlib.voxelize import voxelize
import json
import os


def load_directory(directory, res):
    models = []
    for filename in os.listdir(directory):
        if filename.endswith('.obj'):
            with open(os.path.join(directory, filename)) as f:
                voxels = [v for v in voxelize("models_unprocessed_obj/{}".format(filename), res)] #60
                print("Processed {}. Total voxels generated: {}".format(filename,len(voxels)))
                with open('models/{}_{}.json'.format(res, os.path.splitext(filename)[0]), 'w') as outfile:
                    json.dump(voxels, outfile)
    return models

# filename = "chair1"
# voxels = [v for v in voxelize("models_unprocessed/{}.obj".format(filename), 30)] #60


if __name__ == '__main__':
    # parse cli args
    parser = argparse.ArgumentParser(description='stl/obj file to voxels converter')
    parser.add_argument('directory')
    parser.add_argument('resolution', type=int)
    args = parser.parse_args()
    load_directory(args.directory, args.resolution)
    # for pos_x, pos_y, pos_z in voxelize(args.input, args.resolution):
    #     sys.stdout.write("{}\t{}\t{}\n".format(pos_x, pos_y, pos_z))
