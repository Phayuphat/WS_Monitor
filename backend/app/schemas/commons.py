from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
import datetime

class LineName(BaseModel):
    line_id:int
    line_name:str

class part_no(BaseModel):
    part_id:int
    part_no:str
    part_name:str

class category(BaseModel):
    category:str

class DataWi(BaseModel):
    mode_id: int
    mode:str
    

class wi_table(BaseModel):
    mode_id: int
    mode:str
    










class DataInitals(BaseModel):
    id: int
    part_no:str
    plc_data:str
    updated_at:Optional[datetime.datetime]
    created_at:Optional[datetime.datetime]
    image_path:Optional[List[Dict[str,Any]]] = None
    
class DataInitalsResponse(BaseModel):
    data:List[DataInitals]

################################################
class PostMonitor(BaseModel):
    # id:int 
    process_id: int
    monitor_name: str

class PostData(BaseModel):
    line_id:int
    process_id:int
    part_no:str
    plc_data:str
    image_path:Optional[List[Dict[str,Any]]] = None
    update_at:str

# class DataWi(BaseModel):
#     mode_id: int
#     mode:str
#     update_at:str

# class Display(BaseModel):
#     display_name:str
# class ListDataWi(BaseModel):
#     data:List[DataWi]
#################################################
    









class wi_table(BaseModel):
    id: int
    part_no:str
    plc_data:str
    image_path:Optional[List[Dict[str,Any]]] = None
    # image_path:str
    update_at:str

class delete_a_row(BaseModel):
    id:Union[int, str]