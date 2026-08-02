from app.ai.vector_store import (
    create_collection,
    upsert_product_vector,
    search_similar_products,
)

from app.ai.embedding_service import (
    generate_embedding,
)

create_collection()

products = [
    {
        "id": 1,
        "name": "iPhone 15",
        "category": "Smartphone",
        "brand": "Apple",
        "price": 1200,
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S25",
        "category": "Smartphone",
        "brand": "Samsung",
        "price": 1100,
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "category": "Laptop",
        "brand": "Apple",
        "price": 2400,
    },
    {
        "id": 4,
        "name": "Dell XPS",
        "category": "Laptop",
        "brand": "Dell",
        "price": 1900,
    },
    {
        "id": 5,
        "name": "Nike Air Max",
        "category": "Shoes",
        "brand": "Nike",
        "price": 180,
    },
]

for product in products:

    text = (
        f"{product['name']} "
        f"{product['category']} "
        f"{product['brand']}"
    )

    embedding = generate_embedding(text)

    upsert_product_vector(
        product_id=product["id"],
        embedding=embedding,
        payload=product,
    )

query = generate_embedding(
    "Apple Smartphone"
)

results = search_similar_products(
    embedding=query,
    limit=5,
)
print("\nSearch Results:\n")
for result in results:

    print()

    print(result.payload)

    print(result.score)