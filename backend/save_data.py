import json
from pydantic import BaseModel
from typing import List, Tuple


class ImageData(BaseModel):
    path: str
    shape: Tuple[int, int]
    
class BoxesData(BaseModel):
    cls_id: int
    coords: List[float]
    
    