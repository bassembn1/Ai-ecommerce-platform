from app.jobs.save_event_job import save_event_job
from app.jobs.update_profile_job import update_profile_job
from app.jobs.generate_recommendation_job import (
    generate_recommendation_job,
)



def run(event: dict):

    save_event_job(event)

    update_profile_job(
        event["user_id"]
    )

    generate_recommendation_job(
        event["user_id"]
    )
    

