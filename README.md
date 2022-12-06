# STOREFRONT
Store Front is an online store backend that can be easily combined with any frontend
project.It uses a token based authentication system and supports guest checkout.

## Endpoints

### User Endpoint
   ** USER REGISTRATION **
      Send post request to `/auth/users/` to create user account.
      
  Sample request
  
  ```javascript
    axios.post('/auth/users/', {
    "username": "callisto",
    "password": "r139a",
    "email": "callisto@domain.com",
    "first_name": "Europa",
    "last_name": "Mars"
    }
  ```
      
   ** USER AUTHENTICATION **
      Send post request to `/auth/jwt/create/`
      
  Sample request
      
  ```javascript
     axios.post('/auth/jwt/create', { "username": "callisto", "password": "r139a"})
  ```
  
  Sample Response
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDQwNjMzMywianRpIjoiOWRjNThlMDUwYmQzNDdlYzlkNGI1NWM3M2MwYTIwMDEiLCJ1c2VyX2lkIjoxfQ.1ItVm1Fbci5lRb3aYpqflNS0GSOhUiNGgOVnQlRY7dk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDA2MzMzLCJqdGkiOiJhOWRmMGMwMzcyMzI0NjFmODU0YTE3MWI1NGM4ZjgxYyIsInVzZXJfaWQiOjF9.apUi0cZEjLpodICTdln_JLCKYG7QbCHRGy73VY782xI"
}
  ```
      
      

### Product Endpoint
  Send a GET request `/store/products` to get all products.
  
  Sample Response
  
  ```json
  [
        {
            "id": 648,
            "title": "7up Diet, 355 Ml",
            "description": "tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est",
            "slug": "-",
            "inventory": 82,
            "unit_price": 79.07,
            "price_with_tax": 86.977,
            "collection": 5,
            "images": []
        },
        {
            "id": 905,
            "title": "Absolut Citron",
            "description": "dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et eros",
            "slug": "-",
            "inventory": 32,
            "unit_price": 88.2,
            "price_with_tax": 97.02000000000001,
            "collection": 4,
            "images": []
        }
   ]
  ```
   
   Send a GET request to `/store/products/id` to get a particular product.
   
   Sample Response
    
    ```json
    {
          "id": 648,
          "title": "7up Diet, 355 Ml",
          "description": "tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est",
          "slug": "-",
          "inventory": 82,
          "unit_price": 79.07,
          "price_with_tax": 86.977,
          "collection": 5,
          "images": []
       }
    ```
   
   ### Collection Endpoint
   
   Send a GET request `/store/collections` to get all collections.
   
   Sample Response
    
    ```json
      [
      {
          "id": 1,
          "title": "Flowers",
          "products_count": 0
      },
      {
          "id": 2,
          "title": "Grocery",
          "products_count": 0
      },
      {
          "id": 3,
          "title": "Beauty",
          "products_count": 254
      }
     ]
    ```
 
 ### Cart Endpoint
   Send a POST request `/store/carts` to create a cart.
   
   **Sample Response**
   ```json
   {
    "id": "1f6942a1-b3f4-4a61-ad24-ed41790e88e5",
    "items": [],
    "total_price": 0
   }
   ```
   
   Send a POST request `/store/carts/cart_id/items/` to add items/products to cart.
   
   Send a GET request `/store/carts/cart_id/items/` to get all the contents of a carts
   
   **Sample Request**
   ```javascript
      axios.post(
        '/store/cart/1fc7c18f-6fe0-4eac-9d9f-84386ad6c910/items/',
        {"product_id": 1, "quantity": 10}
      )
   ```
 
 ### Order Endpoint
   Send an authenticated POST request to `/store/orders` with cartto create an order
   
   First add set `Authorization` header in request to token generated from user login
   
   **Sample Request**
   ``` javascript
    axios.defaults.headers.common["authorization"] = `JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDAyNjU1LCJqdGkiOiI1ZDk3YTViNTMxYzQ0M2FhOTkzMjJlYTJhYTdlYmRjNiIsInVzZXJfaWQiOjF9.xyw3rt-RbeBpy_FNgyGi8Z9JVFN2BcXby5Q-GYIW-aY`
    
    axios.post(`/store/orders/`, {cart_id: 1fc7c18f-6fe0-4eac-9d9f-84386ad6c910})
   ```
   Send GET request to `/store/orders` to get orders
   
   **Sample Response**
   ```json
      [
    {
        "id": 1,
        "customer": 1,
        "placed_at": "2022-12-06T09:09:41.072674Z",
        "payment_status": "P",
        "items": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "title": "Bread Ww Cluster",
                    "unit_price": 4.0
                },
                "unit_price": 4.0,
                "quantity": 6
            }
        ]
    }
]
   ```
   
  
 
