from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import CommonsCRUD
from app.schemas.commons import (
DataInitals,DataWi,LineName, part_no,delete_a_row, PostMonitor, category
)
# import json
# from typing import Optional, List, Dict, Any, Union
# import datetime


class CommonsManager:
    def __init__(self) -> None:
        self.crud = CommonsCRUD()

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

    async def get_part_no(
            self,
            
            db: AsyncSession = None,
        ):
            res = await self.crud.get_part_no(db=db)
            return_list = []
            for r in res:
                print(r)
                key_index = r._key_to_index
                return_list.append(
                    part_no(
                        part_id = r[key_index["part_id"]],
                        part_no = r[key_index["part_no"]],
                        part_name = r[key_index["part_name"]],
                    )
                )
            return return_list
    
    async def get_category(
                self,
                db: AsyncSession = None,
            ):
                res = await self.crud.get_category(db=db)
                return_list = []
                for r in res:
                    key_index = r._key_to_index
                    return_list.append(
                        category(
                            category=r[key_index["category"]],
                        )
                    )
                return return_list

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
                        mode_id = r[key_index["mode_id"]],
                        mode = r[key_index["mode"]],
                        
                    )
                )
            return return_list

    async def get_wi_table(
        self,
        line_id=int,
        part_no=str ,
        db: AsyncSession = None,
    ):
        res = await self.crud.get_wi_table(db=db, line_id=line_id, part_no=part_no)
        return_list = []
        for r in res:
            print(r)
            key_index = r._key_to_index
            return_list.append(
                DataWi(
                    mode_id = r[key_index["mode_id"]],
                    mode = r[key_index["mode"]],
                    
                )
            )
        return return_list








    async def update_data(
        self,
        item: DataInitals,
        db: AsyncSession = None,
    ):
        await self.crud.update_data(db=db, item=item)
        return True

    

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