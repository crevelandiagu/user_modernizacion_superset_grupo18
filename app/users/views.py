from app.users.models import ResponseModel, CreateModel
from fastapi import APIRouter
from typing import List
from app.users.actions import (get_all,
                               get_by_id,
                               create_user,
                               turn_admin,
                               delete_user,
                               creacion_usuario,
                               autenticar_usuario)
router = APIRouter()

@router.post("/users", response_model=List[ResponseModel])
def register_users():
    response, status = creacion_usuario()
    return response, status


@router.post("/users/auth", response_model=List[ResponseModel])
def token_user():
    response, status = autenticar_usuario()
    return response, status


@router.get("/", response_model=List[ResponseModel])
def get_users():
    """
    View que retorna lista de usuarios
    """
    return get_all()


@router.get("/{user_id}", response_model=ResponseModel)
def get_user_by_id(user_id: str):
    """
    View que retorna um unico usuario a partir do id
    """
    return get_by_id(user_id)


@router.post("/", response_model=CreateModel, status_code=201)
def create_new_user(new_user: CreateModel):
    """
    View que insere novo usuario
    """
    return create_user(new_user.dict())


@router.put("/{user_id}")
def turn_user_admin(user_id: str):
    """
    View que concede ou retira permissão de administrador do usuario
    """
    return turn_admin(user_id)


@router.delete("/{user_id}")
def delete_user_by_id(user_id: str):
    """
    View que deleta um usuario a partir do id
    """
    return delete_user(user_id)