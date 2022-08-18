from pydantic import BaseModel, Field
from typing import NamedTuple, Union, Literal
from typing_extensions import Annotated

class EditRowAttributes(BaseModel):
    
    table: str
    database: str
    gid: int
    values: object

LonField = Annotated[
    Union[float, int],
    Field(
        title='Coordinate longitude',
        gt=-180,
        lt=180,
    ),
]

LatField = Annotated[
    Union[float, int],
    Field(
        title='Coordinate latitude',
        gt=-90,
        lt=90,
    ),
]

class Coordinates(NamedTuple):
    lon: LonField
    lat: LatField
    
class Geojson(BaseModel):
    type: Literal['Point','MultiPoint','LineString','MultiLineString','Polygon','MultiPolygon']
    coordinates: Coordinates

class EditRowGeometry(BaseModel):
    
    table: str
    database: str
    gid: int
    geojson: Geojson

class AddColumn(BaseModel):
    
    table: str
    database: str
    column_name: str
    column_type: Literal['text','integer','bigint','double precision','booelan','time','uuid']

class DeleteColumn(BaseModel):
    
    table: str
    database: str
    column_name: str

class DeleteRow(BaseModel):
    
    table: str
    database: str
    gid: int

class DeleteTable(BaseModel):
    
    table: str
    database: str