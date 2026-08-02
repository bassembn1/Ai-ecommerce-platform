from pydantic import BaseModel


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    image: str

    class Config:
        from_attributes = True

class ProductCreate(
    BaseModel
):
    title: str
    description: str
    price: float
    image: str