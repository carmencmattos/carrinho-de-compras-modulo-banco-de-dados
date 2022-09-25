from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

#schemas são usados pra validar dados
class UserSchema(BaseModel):
    name: str
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
