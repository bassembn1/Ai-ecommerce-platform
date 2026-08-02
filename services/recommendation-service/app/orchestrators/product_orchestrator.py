from app.jobs.sync_product_job import (
    sync_product_job,
)

from app.jobs.generate_product_embedding_job import (
    generate_product_embedding_job,
)


def run(
    event: dict,
):

    sync_product_job(event)

    generate_product_embedding_job(
        event["product_id"]
    )