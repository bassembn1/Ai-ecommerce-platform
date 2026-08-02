from app.jobs.update_profile_job import update_profile_job
from app.jobs.generate_recommendation_job import (
    generate_recommendation_job,
)


def recommendation_pipeline(
    user_id: int,
):

    update_profile_job(user_id)

    generate_recommendation_job(user_id)