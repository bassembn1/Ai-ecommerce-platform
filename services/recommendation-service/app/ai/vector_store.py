from qdrant_client.models import Distance, PointStruct, VectorParams, PointIdsList

from app.ai.qdrant_client import client

from app.core.config import settings


def create_collection():

    collections = client.get_collections()

    names = [
        c.name
        for c in collections.collections
    ]

    if settings.QDRANT_COLLECTION in names:
        return

    client.create_collection(
        collection_name=settings.QDRANT_COLLECTION,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        ),
    )

def upsert_product_vector(
    product_id: int,
    embedding: list[float],
    payload: dict,
):

    client.upsert(
        collection_name=settings.QDRANT_COLLECTION,
        points=[
            PointStruct(
                id=product_id,
                vector=embedding,
                payload=payload,
            )
        ],
    )

def delete_product_vector(
    product_id: int,
):

    client.delete(
        collection_name=settings.QDRANT_COLLECTION,
        points_selector=PointIdsList(
            points=[product_id],
        ),
    )

def search_similar_products(
    embedding: list[float],
    limit: int = 10,
):

    response = client.query_points(
        collection_name=settings.QDRANT_COLLECTION,
        query=embedding,
        limit=limit,
    )

    return response.points