from typing import List

from pydantic import BaseModel


class Output_cls_JSON(BaseModel):
    old: str
    new: str

class Output_cls_JSON_List(BaseModel):
    list: List[Output_cls_JSON]