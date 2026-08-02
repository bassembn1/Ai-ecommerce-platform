"""from app.database import Base, engine
from app.models import UserEvent

from app.consumer import start_consumer


if __name__ == "__main__":

    Base.metadata.create_all(
        bind=engine
    )

    print(
        "Recommendation Service Started"
    )

    start_consumer()"""

""" from app.database.database import Base, engine
from app.database.models import UserEvent
from app.consumer import start_consumer
from fastapi import FastAPI
from app.database.models import UserEvent, ProductSnapshot

from app.api.router import register_routes
from app.core.config import settings
from app.core.lifespan import lifespan


if __name__ == "__main__":
    print("Tables:", Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)

    print("Tables created successfully")

    print("Recommendation Service Started")

    start_consumer(
        app = FastAPI(
        title="Recommendation Service",
        version="1.0.0",
        lifespan=lifespan,
    ))




    @app.get("/")
    def home():
            return {
                "service": "Recommendation Service",
                "status": "running",
                "version": "1.0.0",
            } 

    register_routes(app)

 """

from fastapi import FastAPI
from app.api.router import register_routes
from app.core.lifespan import lifespan
from app.database.database import Base, engine
from app.database.models import UserEvent, ProductSnapshot
from app.routes.recommendation_route import (
    router as recommendation_router,
)

app = FastAPI(
    title="Recommendation Service",
    version="1.0.0",
    lifespan=lifespan,
)

Base.metadata.create_all(bind=engine)

register_routes(app)







@app.get("/")
def home():
    return {
        "service": "Recommendation Service",
        "status": "running",
        "version": "1.0.0",
    }

