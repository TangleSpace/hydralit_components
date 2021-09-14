from genericpath import isdir
from os import path,listdir,system
        
def build_modules():
    module_directory = path.join(path.abspath(path.dirname(__file__)),"hydralit_components")
    modules = [path.join(module_directory,m) for m in listdir(module_directory) if path.isdir(path.join(module_directory,m))]

    for module in modules:
        mpath = path.join(module,"frontend")
        if path.exists(mpath):
            print(f"Building {mpath}")
            system(f"cd {mpath} && npm i && npm run build")


if __name__ == '__main__':
    build_modules()