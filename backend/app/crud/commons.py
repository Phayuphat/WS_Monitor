from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from app.schemas.commons import (DataInitals, DataWi, delete_a_row, PostMonitor)

def convert_result(res):
    return [{c: getattr(r, c) for c in res.keys()} for r in res]
class CommonsCRUD:
    def __init__(self):
        pass


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

    async def get_part_no(self, db: AsyncSession):  
            
            # line_id = int(line_id)
            # print ("line_id", line_id)
            try:
                stmt = f"""
            SELECT part_id, part_no, part_name FROM main_part
            """
                rs = await db.execute(text(stmt))
                return rs
            except Exception as e:
                raise e
            
    async def get_category(
            self,db: AsyncSession,
        ):
            
            try:
                stmt = f"""
            SELECT category FROM main_category
            """
                rs = await db.execute(text(stmt))
                return rs
            except Exception as e:
                raise e    


    async def get_wi_data(
            self,
            db: AsyncSession,
        ):
            try:
                stmt = f"""
            SELECT * FROM pchart_mode
            """
                rs = await db.execute(text(stmt))
                return rs
            except Exception as e:
                raise e
                
    async def get_wi_table(self, line_id:int, part_no:str, db: AsyncSession,):
            line_id = int(line_id)
            # process_id = int(process_id)
            try:
                
                stmt = f"""
            SELECT mode_id, mode FROM pchart_mode
            WHERE line_id = :line_id AND part_no = :part_no ;
            """
                rs = await db.execute(text(stmt),{"line_id": line_id, "part_no":part_no})
                return rs
            except Exception as e:
                raise e






    async def update_data(self, item:DataInitals, db: AsyncSession):
        stmt = f"""
        UPDATE wi
        SET part_no=:part_no, plc_data=:plc_data
        WHERE id = :id;
        """
        rs = await db.execute(text(stmt), params={"id": item.id,"plc_data":item.plc_data,"part_no":item.part_no})
        await db.commit()  # Corrected the missing parentheses
        return rs

    

    # async def get_part_number(self, line_id:str, process_id:str,
    #     db: AsyncSession,
    # ):
    #     line_id = int(line_id)
    #     process_id = int(process_id)
    #     try:
    #         stmt = f"""
    #     SELECT part_no FROM wi_process
    #     WHERE line_id =:line_id AND process_id =:process_id;
    #     """
    #         rs = await db.execute(text(stmt),{"line_id": line_id, "process_id":process_id})
    #         return rs
    #     except Exception as e:
    #         raise e
    
    
    async def post_edit_data(self,db: AsyncSession,item:DataWi):
        try:
            stmt = f"""
            INSERT INTO wi_process (line_id, process_id, part_no, plc_data, image_path, update_at ) 
            VALUES (:line_id, :process_id, :part_no, :plc_data, cast(:image_path AS jsonb), :update_at )
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
    
    async def post_monitor(self, db: AsyncSession, item: PostMonitor):
        try:
            stmt = """
                INSERT INTO wi_display (process_id, monitor_name) 
                VALUES (:process_id, :monitor_name)
                ON CONFLICT (process_id)
                DO UPDATE SET
                process_id = EXCLUDED.process_id,
                monitor_name = EXCLUDED.monitor_name
                """
            rs = await db.execute(
                text(stmt),
                {
                    "process_id": item.process_id,
                    "monitor_name": item.monitor_name
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

    
    
