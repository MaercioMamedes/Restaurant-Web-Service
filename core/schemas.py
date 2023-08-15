from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    id: int
    description: str
    price: float
    type: str
    model_config = ConfigDict(from_attributes=True)
