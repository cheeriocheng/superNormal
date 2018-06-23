import os
import json

def load_models(directory):
    models = []
    for filename in os.listdir(directory):
        try:
            with open(os.path.join(directory, filename)) as f:
                model = json.load(f)
                models.append(model)
                print('loaded model from file: ' + str(filename))

        except Error:
            print('failed to parse file: ' + str(filename))

    return models

if __name__ == "__main__":
    models = load_models('models')
