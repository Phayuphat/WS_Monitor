from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from fastapi import HTTPException
from typing import Optional, List, Dict, Any, Union
from app.schemas.commons import (
DataInitals,DataWi,delete_a_row
)

def convert_result(res):
    return [{c: getattr(r, c) for c in res.keys()} for r in res]
class CommonsCRUD:
    def __init__(self):
        pass
    
    
    async def get_data_initials(
        self,db: AsyncSession,
    ):
        try:
            stmt = f"""
            SELECT * FROM wi
            """
            rs = await db.execute(
                text(stmt)
            )
            return rs
        except Exception as e:
            print(f"Error during get data: {e}")
            raise HTTPException(status_code=400, detail=f"Bad Requst: {e}")
    

    async def update_data(self, item:DataInitals, db: AsyncSession):
        stmt = f"""
        UPDATE wi
        SET part_no=:part_no, plc_data=:plc_data
        WHERE id = :id;
        """
        rs = await db.execute(text(stmt), params={"id": item.id,"plc_data":item.plc_data,"part_no":item.part_no})
        await db.commit()  # Corrected the missing parentheses
        return rs
    

    async def get_wi_data(
        self,
        db: AsyncSession,
    ):
        try:
            stmt = f"""
        SELECT * FROM wi_process
        """
            rs = await db.execute(text(stmt))
            return rs
        except Exception as e:
            raise e
    
    async def get_linename(
        self,db: AsyncSession,
    ):
        
        try:
            stmt = f"""
        SELECT line_id, line_name FROM main_line
        """
            rs = await db.execute(text(stmt))
            return rs
        except Exception as e:
            raise e

    async def get_process(self,line_id: str, db: AsyncSession):  
        
        line_id = int(line_id)
        print ("line_id", line_id)
        try:
            stmt = f"""
        SELECT process_id, process_name FROM main_process
        WHERE line_id = :line_id ;
        """
            rs = await db.execute(text(stmt),{"line_id": line_id})
            return rs
        except Exception as e:
            raise e
    

    async def get_part_number(self, line_id:str, process_id:str,
        db: AsyncSession,
    ):
        line_id = int(line_id)
        process_id = int(process_id)
        try:
            stmt = f"""
        SELECT part_no FROM wi_process
        WHERE line_id =:line_id AND process_id =:process_id;
        """
            rs = await db.execute(text(stmt),{"line_id": line_id, "process_id":process_id})
            return rs
        except Exception as e:
            raise e
    
    async def get_display(self, process_id:str, db: AsyncSession):
        process_id = int(process_id)
        try:
            stmt = f"""
            SELECT display FROM ws_display 
            WHERE process_id =:process_id;
            """
            rs = await db.execute(text(stmt),{"process_id": process_id})
            return rs
        except Exception as e:
            raise e
        
        
    async def get_wi_table(self,line_id:str, process_id:str,db: AsyncSession,):
        line_id = int(line_id)
        process_id = int(process_id)
        try:
            
            stmt = f"""
        SELECT id, part_no, plc_data, image_path, update_at FROM wi_process
        WHERE line_id = :line_id AND process_id = :process_id ;
        """
            rs = await db.execute(text(stmt),{"line_id": line_id,"process_id":process_id})
            return rs
        except Exception as e:
            raise e
    
    async def post_edit_data(self,db: AsyncSession,item:DataWi):
        try:
            stmt = f"""
            INSERT INTO wi_process (line_id, process_id, part_no, plc_data, image_path, update_at ) 
            VALUES (:line_id, :process_id, :part_no, :plc_data, cast(:image_path AS jsonb),:update_at )
            ON CONFLICT (line_id, process_id, part_no)  
            DO UPDATE SET
            line_id = EXCLUDED.line_id,
            process_id = EXCLUDED.process_id,
            part_no = EXCLUDED.part_no,
            plc_data = EXCLUDED.plc_data,
            image_path = EXCLUDED.image_path,
            update_at = EXCLUDED.update_at
            """
            rs = await db.execute(
                text(stmt),
                        {
                            "line_id": item.line_id,
                            "process_id": item.process_id,
                            "part_no": item.part_no,
                            "plc_data": item.plc_data,
                            "image_path": item.image_path,
                            "update_at": item.update_at
                        }
                    )
            await db.commit()
            return rs
        except Exception as e:
            raise e


    async def delete_row(self,item:delete_a_row, db: AsyncSession):
        try:
            stmt = f"""
            DELETE FROM wi_process
            WHERE id IN (:id) ;
            """
            params ={"id":item.id}
            res = await db.execute(text(stmt), params)
            await db.commit()
            return res
        except Exception as e:
            raise e
        

    async def put_edit_wi(self,item:DataWi, db:AsyncSession):
        try:
            stmt = f"""
            UPDATE wi_process
            SET 
                part_no = :part_no,
                plc_data = :plc_data,
                image_path = cast(:image_path AS jsonb),
                update_at = :update_at
            WHERE id = :id;
            """
            rs = await db.execute(
                    text(stmt),
                            {
                                
                                "part_no": item.part_no,
                                "plc_data": item.plc_data,
                                "image_path": item.image_path,
                                "update_at": item.update_at,
                                "id": item.id,
                            }
                        )
            await db.commit()
            return rs
        except Exception as e:
            raise e

    
    
