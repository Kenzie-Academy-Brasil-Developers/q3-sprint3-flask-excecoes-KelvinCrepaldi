from flask import Flask, jsonify, request
import os
from json import load, dump
from app.functions import verify_json_file
from app.exceptions import EmailExistError, NotTypeStringError

app = Flask(__name__)
FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")


@app.get("/user")
def userget():
    #verifica o arquivo json e o diretorio, cria se não existir
    verify_json_file()

    #return dos dados do json
    with open(f"{FILES_DIRECTORY}database.json", "r") as json_file:
        data = load(json_file)
        return jsonify(data), 200

        

@app.post("/user")
def userpost():
    try:
        #verifica se os tipos do nome e email são string
        if type(request.json["nome"]) is not str or type(request.json["email"]) is not str:
            raise NotTypeStringError()

        #cria um novo usuario, por enquanto sem o ID
        new_user = {}
        new_user["name"] = request.json["nome"].title()
        new_user["email"] = request.json["email"].lower()

        #verifica se o arquivo database.json foi criado, se não ele cria
        verify_json_file() 

        #pega o json do arquivo database.json e cria um id de acordo com o length de "data"
        with open("./app/database/database.json", "r") as json_file:
            json_data = load(json_file)
            new_user["id"] = len(json_data["data"])+1
        
        #verifica se o email já existe
        for user in json_data['data']:
            if user['email'] == new_user['email']:
                raise EmailExistError()

        #adiciona o novo user no dicionario, e escreve o arquivo database.json atualizado
        with open("./app/database/database.json", "w") as json_file:
            json_data["data"].append(new_user)
            dump(json_data, json_file, indent=4)
        
        return jsonify(json_data), 201

    except NotTypeStringError as err:
        return jsonify(err.exception), err.number
    except EmailExistError as err:
        return err.exception, err.number
   
