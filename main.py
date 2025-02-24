from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


class Coords( BaseModel ):
    name: str = 'coords'
    coordX: int
    coordY: int
    coordZ:int





@app.get("/")
def root():
    return "<h1>Test</h1>"


# @app.post( '/coords' )
# def setCoords4( coords: Coords ):

#     return coords




@app.post( '/coords/{coords}' )
def setCoords3( coords: str, seed: int | None = None, worldName: Annotated[ str, Query( min_length = 3, max_length = 20, alias = 'world-name' ) ] = 'My World' ):

    coordsAsArray = coords.split( ',' )

    return {
        'world-name': worldName,
        'seed': seed,
        'coords': {
            'x': int( coordsAsArray[0] ),
            'y': int( coordsAsArray[1] ),
            'z': int( coordsAsArray[2] )
        },
    }



@app.post( '/coords' )
def setCoords2( coordX: int = 0, coordY: int = 0, coordZ: int = 0 ):
    return {
        'recived-coords': {
            'x': coordX,
            'y': coordY,
            'z': coordZ
        }
    }
    

@app.post("/coords/{coords}")
def setCoords( coords: str ):

    coordsAsList = coords.rsplit( ',', -1 )

    return {
        'recived-coords': {
            'x': coordsAsList[0],
            'y': coordsAsList[1],
            'z': coordsAsList[2]
        }
    }