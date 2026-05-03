import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI ()



class Animalcreatedn(BaseModel):
    type: str
    name: str


class AnimalSchema(BaseModel):
    id: int
    type: str
    name: str





@app.post( "/animal_st" )
def create_animal ( body:Animalcreatedn ) :
    
    return {
        "id":1 ,
        "type":body.type,
        "name":body.name,
    }



@app.get( "/animal_st/{id} " )
def get_animal (id : int ) :

    return {
        "id":id,
        "type":"cat",
        "name":"LOPHE"
    }



@app.put("/animal_st/{id}")
def update_animal(id: int, body: Animalcreatedn):
    
    return {
        "id": id,
        "type": body.type,
        "name": body.name
    }



@app.delete("/animal_st/{id}")
def delete_animal(id: int):
    
    return "deleted"







# if __name__ == "__main__":
#     uvicorn.run(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)