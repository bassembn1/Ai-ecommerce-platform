from app.ai.embedding_model import model


def build_product_text(product) -> str:
    """
    Convert a product into text for embedding.
    """

    fields = [
        product.name or "",
        product.category or "",
        product.brand or "",
    ]

    return " ".join(fields)


def generate_embedding(text: str) -> list[float]:
    """
    Generate embedding vector from text.
    """

    embedding = model.encode(text)

    return embedding.tolist()


def generate_product_embedding(product):
    """
    Generate embedding for a product.
    """

    text = build_product_text(product)

    return generate_embedding(text)