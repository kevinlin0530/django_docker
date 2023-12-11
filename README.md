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
        "name": "Example Store",
        "location": "Example Location"
        "update_time":"update_time"
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
    "success": "資料更新成功",
    "data": {
        "name": "Updated Store",
        "location": "Updated Location"
        "update_time":"update_time"
    }
}

## List Stores

```http
GET /api/stores/
```
location (optional): Filter stores by location
name (optional): Filter stores by name

{
    "success": "以下是搜索結果",
    "data": [
        {
            "name": "Example Store",
            "location": "Example Location"
        },
        {
            "name": "Another Store",
            "location": "Another Location"
            "update_time":"update_time"
        }
    ]
}

## List Stores

```http
GET /api/stores/
```

location (optional): Filter stores by location
name (optional): Filter stores by name


{
    "success": "以下是搜索結果",
    "data": [
        {
            "name": "Another Store",
            "location": "Another Location"
            "update_time":"update_time"
        },
        {
            "name": "Another Store",
            "location": "Another Location"
            "update_time":"update_time"
        }
    ]
}

###　Products

## Create a Product

```http
POST /api/products/
```

item: Product name
store_name:store_name
price:price

{
    "success": "產品上架成功",
    "data": {
        "item": "Example Product"
        "store_name":"store_name"
        "price":"price"
        "update_time":"update_time"
        "description":"description"
    }
}


## List Products
```http
GET /api/products/
```
item (optional): Filter products by name


{
    "success": "Products found",
    "data": [
        {
        "item": "以下是搜尋結果"
        "store_name":"store_name"
        "price":"price"
        "update_time":"update_time"
        "description":"description"
        },
        {
        "item": "以下是搜尋結果"
        "store_name":"store_name"
        "price":"price"
        "update_time":"update_time"
        "description":"description"
        }
    ]
}
