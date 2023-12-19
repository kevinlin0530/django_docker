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
```bash
{
    "success": "商店建立完成",
    "data": {
        "name": "Example Store",
        "location": "Example Location"
        "update_time":"update_time"
    }
}
```
## Update a Store

#### Request

```http
PUT /api/stores/{store_id}/
```
Parameters
name: New store name (optional)
location: New store location (optional)

```bash
{
    "success": "資料更新成功",
    "data": {
        "name": "Updated Store",
        "location": "Updated Location"
        "update_time":"update_time"
    }
}
```
## List Stores

#### Request

```http
GET /api/stores/
```
location (optional): Filter stores by location
name (optional): Filter stores by name

```bash
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
```

###　Products

## Create a Product

#### Request

```http
POST /api/products/
```

item: Product name
store_name:store_name
price:price
```bash
{
    "success": "產品上架成功",
    "data": {
        "item": "Example Product",
        "store_name":"store_name",
        "price":"price",
        "update_time":"update_time",
        "description":"description"
    }
}
```

## List Products

#### Request

```http
GET /api/products/
```
item (optional): Filter products by name

```bash
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
```