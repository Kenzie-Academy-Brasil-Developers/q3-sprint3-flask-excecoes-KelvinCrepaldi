from json import dump
import os

def verify_json_file():

    file_dir= "./app/database/database.json"

    #verifica diretorio
    if 'database' not in os.listdir('app'):
        os.mkdir('./app/database')

    #verifica arquivo .json
    for database in os.walk("./app/database"):
        if not 'database.json' in database:
            os.system(f"touch {file_dir}")

    #verifica conteudo do arquivo .json
    if os.path.getsize(file_dir) == 0:
        with open(file_dir , "w") as json_file:
            dump({"data":[]},json_file, indent=4)
