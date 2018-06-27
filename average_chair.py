import load_json
import numpy as np

SIX_NEIGHBORS = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [-1,0,0],
    [0,-1,0],
    [0,0,-1]
    ])

def single_cell(RESOLUTION,THRESHOLD):
    occupiedCubes = []
     #load all the models with the same grid  
    models = load_json.load_folder('models',RESOLUTION )

    # an empty list for holding chair models 
    voxel_matrix = np.zeros((RESOLUTION ,RESOLUTION, RESOLUTION))
    # adding up chairs 
    for chair in models:
        #for each vox written in json file 
        for c in chair: 
            voxel_matrix[c[0],c[1],c[2]] += 1 
    voxel_matrix = np.array(voxel_matrix)/(len(models))
    print("averaging {} chairs".format(len(models)))

    ##create a list of solid cells          
    for x in range(RESOLUTION): 
        for y in range(RESOLUTION): 
            for z in range(RESOLUTION): 
                ## if this voxel is occupied by most models     
                v = voxel_matrix[x,y,z]
                if v > THRESHOLD:
                    occupiedCubes.append([x,y,z])

    return occupiedCubes 


def neighbors(RESOLUTION,THRESHOLD):
    THRESHOLD  = 1.5
    occupiedCubes = []
     #load all the models with the same grid  
    models = load_json.load_folder('models',RESOLUTION )

    # an empty list for holding chair models 
    voxel_matrix = np.zeros((RESOLUTION ,RESOLUTION, RESOLUTION))
    # adding up chairs 
    for chair in models:
        #for each vox written in json file 
        for c in chair: 
            voxel_matrix[c[0],c[1],c[2]] += 1 
    voxel_matrix = np.array(voxel_matrix)/(len(models))
    print("averaging {} chairs".format(len(models)))

    for x in range(1,RESOLUTION-1): 
      for y in range(1,RESOLUTION-1): 
          for z in range(1, RESOLUTION-1): 
              ## counting neighbors 
              neighour_sum = 0
              for n in SIX_NEIGHBORS:
                  p = np.array([x,y,z])+n
                  neighour_sum += voxel_matrix[p[0],p[1],p[2]]
              neighour_sum += voxel_matrix[x,y,z]   
              # print("{}\t{}\t{}\t{}".format(x,y,z,neighour_sum))  
              if neighour_sum > THRESHOLD:
                  occupiedCubes.append([x,y,z])


    return occupiedCubes 

def build_neighbor_dict(voxel_matrix, center_ind, dict):
  ## TODO edge cases: out of boundary 
  for n in SIX_NEIGHBORS:
      p = np.array(center_ind) + n #neighour index
      # if [tuple(p)] not in dict:
      dict[tuple(p)] = voxel_matrix[p[0],p[1],p[2]]
      if tuple(center_ind) in dict: 
        del dict[tuple(center_ind)]


def flood(RESOLUTION,THRESHOLD):
    occupiedCubes = []
     #load all the models with the same grid  
    models = load_json.load_folder('models',RESOLUTION )

    # an empty list for holding chair models 
    voxel_matrix = np.zeros((RESOLUTION ,RESOLUTION, RESOLUTION))
    # adding up chairs 
    for chair in models:
        #for each vox written in json file 
        for c in chair: 
            voxel_matrix[c[0],c[1],c[2]] += 1 
    voxel_matrix = np.array(voxel_matrix)/(len(models))
    print("averaging {} chairs".format(len(models)))

    neighbor_dict = {}
    max_ind = np.unravel_index(voxel_matrix.argmax(), voxel_matrix.shape)
    build_neighbor_dict(voxel_matrix, max_ind, neighbor_dict)
    ## todo exclude the ones that are already added to the occupideCubes list 
    while len(occupiedCubes) < 1000: 
        s = [(k, neighbor_dict[k]) for k in sorted(neighbor_dict, key=neighbor_dict.get, reverse=True)]
        t = next(iter(neighbor_dict))
        if voxel_matrix[t] >0.1:
          occupiedCubes.append(t)
          print("total neighbor length {}".format(len(neighbor_dict)))
          print("Adding voxel {}. value {}".format (t,voxel_matrix[t] ))
          build_neighbor_dict(voxel_matrix, t , neighbor_dict)
        else:
          break

    
    
    return occupiedCubes 


if __name__ == "__main__":
    print("averaging module")
