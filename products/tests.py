from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Product

class ProductTests(TestCase):
    def setUp(self):
        # Crie dados de teste com base no JSON fornecido
        self.product_data = {
            "code": 202,
            "status": "trash",
            "imported_t": "2023-09-04T16:17:05Z",
            "url": "http://google.com",
            "creator": "eyudsfffffffffff",
            "created_t": "20230904161715",
            "last_modified_t": "20230904161716",
            "product_name": "sefsefsef",
            "quantity": "sefsefsef",
            "brands": "sefsefsef",
            "categories": "sefsefsef",
            "labels": "sefsefsef",
            "cities": "sefsef",
            "purchase_places": "sefsef",
            "stores": "sefsef",
            "ingredients_text": "sefsefsefsefsfsefsef  fsefsefsefsefsf",
            "traces": "sfesesf",
            "serving_size": "sfsef",
            "serving_quantity": "13.70",
            "nutriscore_score": 5,
            "nutriscore_grade": "a",
            "main_category": "awdawdawdadw",
            "image_url": "http://google.com"
    }

    
        # Crie um produto com base nos dados de teste
        self.product = Product.objects.create(**self.product_data)

    def test_product_detail_view(self):
        # Teste a view que mostra detalhes de um produto específico
        response = self.client.get(reverse('product-detail', args=[self.product_data['code']]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.product_data['code'])
        self.assertEqual(response.data['product_name'], self.product_data['product_name'])

    def test_product_list_view(self):
        # Teste a view que lista todos os produtos
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_create_view(self):
        # Teste a view que cria um produto
        new_product_data = {
            "code": 12345678,
            "status": "published",
            "imported_t": "2023-09-04T16:17:05Z",
            "url": "http://google.com",
            "creator": "eyudsfffffffffff",
            "created_t": "20230904161715",
            "last_modified_t": "20230904161716",
            "product_name": "sefsefsef",
            "quantity": "sefsefsef",
            "brands": "sefsefsef",
            "categories": "sefsefsef",
            "labels": "sefsefsef",
            "cities": "sefsef",
            "purchase_places": "sefsef",
            "stores": "sefsef",
            "ingredients_text": "sefsefsefsefsfsefsef  fsefsefsefsefsf",
            "traces": "sfesesf",
            "serving_size": "sfsef",
            "serving_quantity": "13.70",
            "nutriscore_score": 5,
            "nutriscore_grade": "a",
            "main_category": "awdawdawdadw",
            "image_url": "http://google.com"}
        response = self.client.post(reverse('product-list'), new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # Verifique se um novo produto foi criado

        def test_product_update_view(self):
            # Teste a view que permite atualizar um produto
            updated_data = {
                "status": "updated",
                "product_name": "Produto Atualizado",
                "quantity": "400 g",
                "brands": "Nova Marca",
                "categories": "Nova Categoria",
                "labels": "Novos Rótulos",
                "cities": "Nova Cidade",
                "purchase_places": "Novos Locais de Compra",
                "stores": "Novas Lojas",
                "ingredients_text": "Novos Ingredientes",
                "traces": "Novas Traços",
                "serving_size": "Nova Tamanho da Porção",
                "serving_quantity": 42.0,
                "nutriscore_score": 18,
                "nutriscore_grade": "c",
                "main_category": "Nova Categoria Principal",
                "image_url": "https://nova-imagem.com/imagem.jpg"
            }

            # Realize uma solicitação PUT para atualizar o produto
            response = self.client.put(reverse('product-detail', args=[self.product_data['code']]), updated_data, format='json')

            # Verifique se a resposta tem status HTTP 200 OK
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            # Recarregue o objeto Product do banco de dados
            self.product.refresh_from_db()

            # Verifique se os campos atualizados correspondem aos valores esperados
            self.assertEqual(self.product.status, updated_data['status'])
            self.assertEqual(self.product.product_name, updated_data['product_name'])
            self.assertEqual(self.product.quantity, updated_data['quantity'])
            self.assertEqual(self.product.brands, updated_data['brands'])
            self.assertEqual(self.product.categories, updated_data['categories'])
            self.assertEqual(self.product.labels, updated_data['labels'])
            self.assertEqual(self.product.cities, updated_data['cities'])
            self.assertEqual(self.product.purchase_places, updated_data['purchase_places'])
            self.assertEqual(self.product.stores, updated_data['stores'])
            self.assertEqual(self.product.ingredients_text, updated_data['ingredients_text'])
            self.assertEqual(self.product.traces, updated_data['traces'])
            self.assertEqual(self.product.serving_size, updated_data['serving_size'])
            self.assertEqual(self.product.serving_quantity, updated_data['serving_quantity'])
            self.assertEqual(self.product.nutriscore_score, updated_data['nutriscore_score'])
            self.assertEqual(self.product.nutriscore_grade, updated_data['nutriscore_grade'])
            self.assertEqual(self.product.main_category, updated_data['main_category'])
            self.assertEqual(self.product.image_url, updated_data['image_url'])

        def test_product_delete_view(self):
            # Teste a view que exclui um produto
            response = self.client.delete(reverse('product-detail', args=[self.product_data['code']]))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(Product.objects.count(), 0)  # Verifique se o produto foi excluído com sucesso