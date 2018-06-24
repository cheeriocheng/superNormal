'''
load all jsonmodels from a folder 
''' 
import os
import json

def load_folder(directory):
    models = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(directory, filename)) as f:
                    model = json.load(f)
                    models.append(model)
                    print('loaded model from file: ' + str(filename))

            except:
                print('failed to parse file: ' + str(filename))

    return models

if __name__ == "__main__":
    models = load_models('models')
