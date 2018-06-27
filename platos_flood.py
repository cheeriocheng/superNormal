import load_json
import numpy as np
from math import floor

# generate 3d matrix with sum of chair voxels in each cell
def generate_average_voxel_matrix (resolution):

    # load models
    models = load_json.load_folder('models', resolution)

    # empty 3d matrix of ints to hold value sums
    voxel_matrix = np.zeros((resolution, resolution, resolution), np.int8)

    # sum chair voxels into matrix
    voxel_count = 0
    for chair in models:
        for vox in chair:
            voxel_matrix[vox[0], vox[1], vox[2]] += 1
            voxel_count += 1

    return voxel_matrix, floor(voxel_count / len(models))

def distance (coords, resolution):
    half = floor(resolution / 2)
    d = 0
    for coord in coords:
        d += abs(coord - half)

    return -d

def platos_flood (resolution):

    # get matrix with # of chair voxels at each cell & average vox per chair
    voxel_matrix, avg_vox = generate_average_voxel_matrix(resolution)

    print("average voxels per chair: ", avg_vox)

    # start with first highest value voxel
    max_voxels = []
    max_value = voxel_matrix[
        np.unravel_index(voxel_matrix.argmax(), voxel_matrix.shape)]
    for x in range(resolution):
        for y in range(resolution):
            for z in range(resolution):
                if voxel_matrix[x, y, z] == max_value:
                    dist = distance((x, y, z), resolution)

                    # store voxels as tuple with value first 
                    # -> (value, distance, x, y, z)
                    max_voxels.append((max_value, dist, x, y, z))


    seed = sorted(max_voxels).pop()

    print("seed: ", seed)

    # start neighbors set with seed and add highest neighbor to platos chair
    # until average # of voxels per chair reached
    neighbors = set([seed])
    platos = set()
    while len(platos) < avg_vox:

        # find next voxel with highest value from neighbors & add to platos
        next_vox = sorted(neighbors).pop()
        neighbors.remove(next_vox)
        platos.add(next_vox)

        # add next voxels neighbors to neighbors
        for x, y, z in [(-1,0,0),(0,-1,0),(0,0,-1),(1,0,0),(0,1,0),(0,0,1)]:
            coords = (x + next_vox[2], y + next_vox[3], z + next_vox[4])
            if min(coords) > -1 and max(coords) < resolution:
                value = voxel_matrix[coords]
                dist = distance(coords, resolution)
                neighbor_vox = (value, dist, coords[0], coords[1], coords[2])
                if neighbor_vox not in platos:
                    neighbors.add(neighbor_vox)

        print("*", next_vox)

    # strip out values and just return [x, y, z] coords lists
    return [list(coords[2:]) for coords in platos]

if __name__ == "__main__":
    platos_chair = platos_flood(60)
