'''
load all jsonmodels from a folder 
''' 
import os
import json

def load_folder(directory, res):
    models = []
    for filename in os.listdir(directory):
        if filename.endswith('.json') and filename.startswith(str(res)):
            try:
                with open(os.path.join(directory, filename)) as f:
                    model = json.load(f)
                    models.append(model)
                    print('Loaded file: ' + str(filename))

            except:
                print('failed to parse file: ' + str(filename))

    return models

if __name__ == "__main__":
    models = load_models('models')
