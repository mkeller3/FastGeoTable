from fastapi import APIRouter, Request, HTTPException
import json

router = APIRouter()

import models

@router.post("/edit_row_attributes/", tags=["Tables"])
async def edit_row_attributes(
        request: Request,
        info: models.EditRowAttributes
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:
        sql_field_query = f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{info.table}'
        AND column_name != 'geom';
        """

        db_fields = await con.fetch(sql_field_query)

        db_columns = []

        db_column_types = {}

        for field in db_fields:
            db_columns.append(field['column_name'])
            db_column_types[field['column_name']] = field['data_type']

        string_columns = ",".join(db_columns)

        query = f"""
            UPDATE "{info.table}"
            SET 
        """

        numeric_field_types = ['integer','double precision']

        for field in info.values:
            if field not in db_columns:
                raise HTTPException(status_code=400, detail=f"Column: {field} is not a column for {info.table}. Please use one of the following columns. {string_columns}")
            if db_column_types[field] in numeric_field_types: 
                query += f"{field} = {info.values[field]},"
            else:
                query += f"{field} = '{info.values[field]}',"
        
        query = query[:-1]

        query += f" WHERE gid = {info.gid};"

        await con.fetch(query)

        return {"status": True}

@router.post("/edit_row_geometry/", tags=["Tables"])
async def edit_row_geometry(
        request: Request,
        info: models.EditRowGeometry
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:

        geojson = {
            "type": info.geojson.type,
            "coordinates": json.loads(json.dumps(info.geojson.coordinates))
        }

        query = f"""
            UPDATE "{info.table}"
            SET geom = ST_GeomFromGeoJSON('{json.dumps(geojson)}')
            WHERE gid = {info.gid};
        """

        await con.fetch(query)
        
        return {"status": True}

@router.post("/add_column/", tags=["Tables"])
async def add_column(
        request: Request,
        info: models.AddColumn
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:

        query = f"""
            ALTER TABLE "{info.table}"
            ADD COLUMN "{info.column_name}" {info.column_type};
        """

        await con.fetch(query)
        
        return {"status": True}

@router.delete("/delete_column/", tags=["Tables"])
async def delete_column(
        request: Request,
        info: models.DeleteColumn
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:
        
        query = f"""
            ALTER TABLE "{info.table}"
            DROP COLUMN IF EXISTS "{info.column_name}";
        """

        await con.fetch(query)
        
        return {"status": True}


@router.delete("/delete_row/", tags=["Tables"])
async def delete_row(
        request: Request,
        info: models.DeleteRow
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:
        
        query = f"""
            DELETE FROM "{info.table}"
            WHERE gid = {info.gid};
        """

        await con.fetch(query)
        
        return {"status": True}


@router.delete("/delete_table/", tags=["Tables"])
async def delete_table(
        request: Request,
        info: models.DeleteTable
    ):

    pool = request.app.state.databases[f'{info.database}_pool']

    async with pool.acquire() as con:
        
        query = f"""
            DROP TABLE IF EXISTS "{info.table}";
        """

        await con.fetch(query)
        
        return {"status": True}