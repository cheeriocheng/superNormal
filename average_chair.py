import load_json
import numpy as np

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
    THRESHOLD  = 1.4
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

    neighours = np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1],
        [-1,0,0],
        [0,-1,0],
        [0,0,-1]
        ])
    for x in range(1,RESOLUTION-1): 
      for y in range(1,RESOLUTION-1): 
          for z in range(1, RESOLUTION-1): 
              ## counting neighbors 
              neighour_sum = 0
              for n in neighours:
                  p = np.array([x,y,z])+n
                  neighour_sum += voxel_matrix[p[0],p[1],p[2]]
              # print("{}\t{}\t{}\t{}".format(x,y,z,neighour_sum))  
              if neighour_sum > THRESHOLD:
                  occupiedCubes.append([x,y,z])


    return occupiedCubes 


def random_walk(RESOLUTION,THRESHOLD):
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

    max_ind = np.unravel_index(voxel_matrix.argmax(), voxel_matrix.shape)
    
    ##TODO 
    
    return occupiedCubes 


if __name__ == "__main__":
    print("averaging module")
