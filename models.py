from pydantic import BaseModel

class EditRowAttributes(BaseModel):
    
    table: str
    database: str
    gid: int
    values: object