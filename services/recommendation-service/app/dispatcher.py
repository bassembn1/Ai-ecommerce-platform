from app.jobs.save_event_job import save_event_job
from app.jobs.sync_product_job import sync_product_job
from app.orchestrators.recommendation_orchestrator import run
from app.orchestrators.product_orchestrator import (
    run as run_product_pipeline,
)


def dispatch_event(event: dict):

    event_type = event["event_type"]

    if event_type in {
        "view_product",
        "add_to_cart",
        "purchase",
    }:
        run(event)

    elif event_type in {
        "product_created",
        "product_updated",
    }:
       run_product_pipeline(event)

    else:
        print(f"Unknown event: {event_type}")