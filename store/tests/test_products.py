import pytest
from rest_framework import status
from store.models import Collection, Product
from model_bakery import baker


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    product = {
        'title': 'a',
        'description': 'abc',
        'inventory': 10,
        'unit_price': 4.5,
        'slug': '-',
    }

    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product(self.product)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_product, authenticate):
        authenticate()

        response = create_product(self.product)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_product, authenticate):
        product = self.product.copy()
        product['title'] = ''
        authenticate(is_staff=True)

        response = create_product(product)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, create_product, authenticate):
        product = self.product.copy()
        collection = baker.make(Collection)
        product['collection'] = collection.id
        authenticate(is_staff=True)

        response = create_product(product)

        print(response.data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exits_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        # assert response.data == {
        #     'id': product.id,
        #     'title': product.title,
        #     'inventory': product.inventory,
        #     'unit_price': product.unit_price,
        #     'description': product.description,
        #     'slug': product.slug,
        #     'collection': product.collection,
        #     'images': product.images,
        #     'price_with_tax': product.calculate_tax
        # }

    def test_if_product_not_exits_returns_404(self, api_client):
        product_id = 0

        response = api_client.get(f'/store/products/{product_id}/')

# @pytest.mark.django_db
# class TestPatchProduct:
