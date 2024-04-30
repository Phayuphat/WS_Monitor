from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import CommonsCRUD
from app.schemas.commons import (
DataInitals,DataWi,LineName, process_data,part_no,wi_table,delete_a_row,display, PostMonitor
)
import json
from typing import Optional, List, Dict, Any, Union
import datetime


class CommonsManager:
    def __init__(self) -> None:
        self.crud = CommonsCRUD()

    async def update_data(
        self,
        item: DataInitals,
        db: AsyncSession = None,
    ):
        await self.crud.update_data(db=db, item=item)
        return True


    async def get_wi_data(
        self,
        db: AsyncSession = None,
    ):
        res = await self.crud.get_wi_data(db=db)
        return_list = []
        for r in res:
            key_index = r._key_to_index
            return_list.append(
                DataWi(
                    id=r[key_index["id"]],
                    plc_data=r[key_index["plc_data"]],
                    part_no=r[key_index["part_no"]],
                    image_path=r[key_index["image_path"]],
                    update_at=r[key_index["update_at"]],
                )
            )
        return return_list
    

    async def get_linename(
        self,
        db: AsyncSession = None,
    ):
        res = await self.crud.get_linename(db=db)
        return_list = []
        for r in res:
            key_index = r._key_to_index
            return_list.append(
                LineName(
                    line_id=r[key_index["line_id"]],
                    line_name=r[key_index["line_name"]],
                )
            )
        return return_list
    

    async def get_process(
        self,
        line_id=str,
        db: AsyncSession = None,
    ):
        print("manager",line_id)
        res = await self.crud.get_process(db=db,line_id=line_id)
        return_list = []
        for r in res:
            print(r)
            key_index = r._key_to_index
            return_list.append(
                process_data(
                    process_id=r[key_index["process_id"]] ,
                    process_name=r[key_index["process_name"]],
                )
            )
        return return_list
    

    async def get_part_number(
        self,
        line_id=int,
        process_id=int,
        db: AsyncSession = None,
    ):
        res = await self.crud.get_part_number(db=db, line_id=line_id, process_id=process_id)
        return_list = []
        for r in res:
            print(r)
            key_index = r._key_to_index
            return_list.append(
                part_no(
                    part_no=r[key_index["part_no"]],
                )
            )
        return return_list

    async def get_display(
        self, 
        process_id: str, 
        db: AsyncSession = None
        ):
        res = await self.crud.get_display(db=db, process_id=process_id)
        return_list = []
        for r in res:
            print(r)
            key_index = r._key_to_index
            return_list.append(
                display(
                    monitor_name=r[key_index["monitor_name"]],
                    monitor_id=r[key_index["monitor_id"]]
                )
            )
        return return_list



    async def get_wi_table(
        self,
        line_id=str,
        process_id=str ,
        db: AsyncSession = None,
    ):
        res = await self.crud.get_wi_table(db=db, line_id=line_id, process_id=process_id)
        return_list = []
        for r in res:
            print(r)
            key_index = r._key_to_index
            return_list.append(
                DataWi(
                    id=r[key_index["id"]],
                    part_no=r[key_index["part_no"]],
                    plc_data=r[key_index["plc_data"]],
                    image_path=r[key_index["image_path"]],
                    update_at=r[key_index["update_at"]],
                )
            )
        return return_list
    

    async def post_edit_data(
        self,
        item: DataWi,
        db: AsyncSession = None,
    ):
        print("edit",item)
        await self.crud.post_edit_data(db=db, item=item)
        return True

    async def post_monitor(
        self,
        item: PostMonitor,
        db: AsyncSession = None,
    ):
        print("monitor_manager",item)
        await self.crud.post_monitor(db=db, item=item)
        return True


    async def delete_row(
        self,
        item:delete_a_row,
        db:AsyncSession = None,
    ):
        print("delete",item)
        await self.crud.delete_row(db=db, item=item)
        return True
    
    async def put_edit_wi(
            self,
            item:DataWi,
            db:AsyncSession = None,
    ):
        print("update", item)
        await self.crud.put_edit_wi(db=db, item=item)
        return True