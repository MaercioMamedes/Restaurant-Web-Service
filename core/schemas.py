from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    description: str
    price: float
    type: str
    model_config = ConfigDict(from_attributes=True)


class ProductPublic(ProductSchema):
    id: int
