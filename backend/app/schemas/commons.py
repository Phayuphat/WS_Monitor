from pydantic import BaseModel
from typing import Optional, List, Dict, Any, Union
import datetime


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
    process_id: int
    monitor_name: str

class PostData(BaseModel):
    line_id:int
    process_id:int
    part_no:str
    plc_data:str
    image_path:Optional[List[Dict[str,Any]]] = None
    update_at:str

class DataWi(BaseModel):
    id: int
    part_no:str
    plc_data:str
    update_at:str
    image_path:Optional[List[Dict[str,Any]]] = None

class Display(BaseModel):
    display_name:str
class ListDataWi(BaseModel):
    data:List[DataWi]
#################################################
    
class LineName(BaseModel):
    line_id:int
    line_name:str

class LineName_data(BaseModel):
    value:List[LineName]

############################
    
class process_data(BaseModel):
    process_id:int
    process_name:str
    

class process_dataResponse(BaseModel):
    process_name:List[process_data]
    
#############################
    
class part_no(BaseModel):
    part_no:str
class part_number_data(BaseModel):
    part_number_name:List[part_no]

class display(BaseModel):
    monitor_name:str
class display_data(BaseModel):
    monitor_name:List[display]

    
class wi_table(BaseModel):
    id: int
    part_no:str
    plc_data:str
    image_path:Optional[List[Dict[str,Any]]] = None
    # image_path:str
    update_at:str

class delete_a_row(BaseModel):
    id:Union[int, str]