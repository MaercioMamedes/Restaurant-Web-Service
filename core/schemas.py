from pydantic import BaseModel, ConfigDict, EmailStr


class ProductSchema(BaseModel):
    description: str
    price: float
    type: str
    model_config = ConfigDict(from_attributes=True)


class ProductPublic(ProductSchema):
    id: int


class ProductList(BaseModel):
    products: list[ProductPublic]


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublic(UserSchema):
    id: int
    name: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Message(BaseModel):
    msg: str
