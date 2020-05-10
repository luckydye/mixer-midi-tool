import json
import os 

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

class Config:

    datastore = None

    def save(self):
        json_file  = open(get_path() + "\config.json", "w") 
        json_string = json.dumps(self.datastore, indent=4)
        json_file.write(json_string)

    def load(self):
        json_file  = open(get_path() + "\config.json", "r") 
        json_string = json_file.read()
        self.datastore = json.loads(json_string)
        print(self.datastore)

    def get(self, key):
        return self.datastore[key]

    def set(self, key, value):
        self.datastore[key] = value
        self.save()