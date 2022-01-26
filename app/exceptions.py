from flask import request
class EmailExistError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exception = {"error": "User already exists."}
        self.number = 409

class NotTypeStringError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        typeName = str(type(request.json["nome"]))[8:-2]
        typeEmail = str(type(request.json["email"]))[8:-2]

        self.exception = {"wrong fields": [

        
        {
            "nome": f"{typeName}"
        },
        {
            "email": f"{typeEmail}"
        }
    ]
}
        self.number = 400