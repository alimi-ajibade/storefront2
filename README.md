# STOREFRONT
Store Front is an online store backend that can be easily combined with any frontend
project.It uses a token based authentication system and supports guest checkout.

## Endpoints
### Product List
  `/store/products` to get all product list
  Sample Response
  `[
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
   ]`
2. Product detials
3. Collection List
4. Collection Details
