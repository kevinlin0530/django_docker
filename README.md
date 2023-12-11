# Django Shopping System

This project implements a simple shopping system using Django.

## Table of Contents

- [Stores](#stores)
- [Products](#products)
- [Users](#users)
- [Purchases](#purchases)

## Stores

### Create a Store

#### Request

```http
POST /api/stores/
```

Parameters
name: Store name
location: Store location

{
    "success": "商店建立完成",
    "data": {
        "id": 1,
        "name": "Example Store",
        "location": "Example Location"
    }
}

## Update a Store

```http
PUT /api/stores/{store_id}/
```
Parameters
name: New store name (optional)
location: New store location (optional)

{
    "success": "Store updated successfully",
    "data": {
        "id": 1,
        "name": "Updated Store",
        "location": "Updated Location"
    }
}

## List Stores

```http
GET /api/stores/
```
location (optional): Filter stores by location
name (optional): Filter stores by name

{
    "success": "Stores found",
    "data": [
        {
            "id": 1,
            "name": "Example Store",
            "location": "Example Location"
        },
        {
            "id": 2,
            "name": "Another Store",
            "location": "Another Location"
        }
    ]
}
