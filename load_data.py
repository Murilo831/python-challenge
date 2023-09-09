import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge.settings')
django.setup()

import csv
from products.models import Product  # Importe seu modelo Product aqui

# Abra o arquivo CSV para leitura
with open('export1.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        # Crie uma instância do modelo Product com os valores das colunas
        product = Product(
            code=row['code'],
            status=row['status'],
            imported_t=row['imported_t'],
            url=row['url'],
            creator=row['creator'],
            created_t=row['created_t'],
            last_modified_t=row['last_modified_t'],
            product_name=row['product_name'],
            quantity=row['quantity'],
            brands=row['brands'],
            categories=row['categories'],
            labels=row['labels'],
            cities=row['cities'],
            purchase_places=row['purchase_places'],
            stores=row['stores'],
            ingredients_text=row['ingredients_text'],
            serving_size=row['serving_size'],
            serving_quantity=row['serving_quantity'],
            nutriscore_score=row['nutriscore_score'],
            nutriscore_grade=row['nutriscore_grade'],
            main_category=row['main_category'],
            image_url=row['image_url']
        )
        
        # Salve a instância no banco de dados
        product.save()