from pydantic import BaseModel


class CreateModel(BaseModel):
    id = int
    username = str
    email = str
    first_name = str
    last_name = str
    is_active = bool
    is_anonymous = bool

class ResponseModel(CreateModel):
    id: str
