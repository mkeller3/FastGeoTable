# FastGeoTable

FastGeoTable is a geospatial api to edit tables with geospatial data. FastGeoTable is written in [Python](https://www.python.org/) using the [FastAPI](https://fastapi.tiangolo.com/) web framework. 

---

**Source Code**: <a href="https://github.com/mkeller3/FastGeoTable" target="_blank">https://github.com/mkeller3/FastGeoTable</a>

---

## Requirements

FastGeoTable requires PostGIS >= 2.4.0.

## Configuration

In order for the api to work you will need to edit the `config.py` file with your database connections.

Example
```python
DATABASES = {
    "data": {
        "host": "localhost", # Hostname of the server
        "database": "data", # Name of the database
        "username": "postgres", # Name of the user, ideally only SELECT rights
        "password": "postgres", # Password of the user
        "port": 5432, # Port number for PostgreSQL
    }
}
```

## Usage

### Running Locally

To run the app locally `uvicorn main:app --reload`

### Production
Build Dockerfile into a docker image to deploy to the cloud.

## API

| Method | URL                                                                              | Description                                             |
| ------ | -------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `PUT`  | `/api/v1/tables/edit_row_attributes`                                             | [Edit Row Attributes](#edit-row-attributes)               |
| `PUT`  | `/api/v1/tables/edit_row_geometry`                                               | [Edit Row Geometry](#edit-row-geometry)               |
| `POST`  | `/api/v1/tables/add_column`                                                     | [Add Column](#add-column)               |
| `DELETE`  | `/api/v1/tables/delete_column`                                                | [Delete Column](#delete-column)               |
| `POST`  | `/api/v1/tables/add_row`                                                        | [Add Row](#add-row)               |
| `DELETE`  | `/api/v1/tables/delete_row`                                                   | [Delete Row](#delete-row)               |
| `DELETE`  | `/api/v1/tables/delete_table`                                                 | [Delete Table](#delete-table)               |
| `POST`  | `/api/v1/tables/create_table`                                                   | [Create Table](#create-table)               |
| `GET`  | `/api/v1/health_check`                                                           | Server health check: returns `200 OK`   |

## Endpoint Description's

## Edit Row Attributes

### Description
Edit Row Attributes endpoint allows you to edit one/all atrributes for a row at a time.
In the example below we are changing the `objectid` and `last_name` columns for the row with a gid of `1`.


Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "mclean_county_parcels",
    "gid": 1,
    "values": {
        "objectid": "1",
        "last_name": "sample"
    }
}
```

### Example Output
```json
{
    "status": true
}
```

## Edit Row Geometry

### Description
Edit Row Geometry endpoint allows you to change the geometry for each feature in a table by passing in geojson geometry in SRID 4326.
In the example below, we are updating the zip centroid with the gid of `1` for a new lat lng of `[-88.23456,40.12345]`.

Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "zip_centroids",
    "gid": 1,
    "geojson": {
        "type": "Point",
        "coordinates": [
            -88.23456,
            40.12345
        ]
    }
}
```

### Example Output
```json
{
    "status": true
}
```

## Add Column

### Description


Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "zip_centroids",
    "column_name": "test",
    "column_type": "text"
}
```

### Example Output
```json
{
    "status": true
}

```

## Delete Column

### Description


Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "zip_centroids",
    "column_name": "test"
}
```

### Example Output
```json
{
    "status": true
}
```

## Add Row

### Description


Example: 
### Example Input 
```json

```

### Example Output
```json

```
## Delete Row

### Description


Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "zip_centroids",
    "gid": 1
}
```

### Example Output
```json
{
    "status": true
}
```

## Create Table

### Description


Example: 
### Example Input 
```json

```

### Example Output
```json
{
    "status": true
}
```

## Delete Table

### Description


Example: 
### Example Input 
```json
{
    "database": "data",
    "table": "zip_centroids"
}
```

### Example Output
```json
{
    "status": true
}
```