from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    description: str
    price: float
    type: str
