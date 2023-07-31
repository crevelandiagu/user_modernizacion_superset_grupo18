import secrets
import hashlib
from typing import List, Dict, Any
from schemas import User
from app.config.db import session, save, commit
from datetime import timedelta, datetime
from flask_jwt_extended import create_access_token

UserInterface = Dict[Any, Any]

def get_all() -> List[UserInterface]:
    return [user.serializer() for user in session.query(User)]

def get_by_id( user_id: int) -> UserInterface:
    return session.query(User).filter(user_id == User.id).first().serializer()

def create_user(new_user: UserInterface) -> UserInterface:
    new_user["is_active"] = True
    new_user["is_admin"] = False
    save(User(**new_user))
    return new_user


def turn_admin(user_id):
    user = get_by_id(user_id)
    print(f'User before change status {user["is_admin"]}')
    user['is_admin'] = False if user['is_admin'] == True else True
    print(f'User after change status {user["is_admin"]}')
    commit()
    return 'ok', 200

def delete_user(user_id: int) -> UserInterface:
    user = get_by_id(user_id)
    user['is_active'] = False
    commit()
    return 'ok', 200

def creacion_usuario(request):

    try:
        existe_usuario = User.query.filter(User.username == request.json["username"]).first()
        existe_email = User.query.filter(User.email == request.json["email"]).first()
        if existe_usuario is not None or existe_email is not None:
            return {"mensaje": "El usuario ya existe, pruebe con otro"}, 412

        salt = secrets.token_hex(8)
        password = f"{request.json['password']}{salt}"

        nuevo_usuario = User(
            username=request.json["username"],
            email=request.json["email"],
            password=hashlib.sha256(password.encode()).hexdigest(),
            salt=salt,
        )
        save(nuevo_usuario)
        commit()
        return {"id": nuevo_usuario.id, "createdAt": datetime.now().isoformat()}, 201
    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400

def autenticar_usuario(request):
    try:

        usuario_auth = User.query.filter(User.username == request.json["username"]).first()

        if usuario_auth is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        password_input = f"{request.json['password']}{usuario_auth.salt}"
        password = User.query.filter(User.username == request.json["username"],
                                         User.password == hashlib.sha256(password_input.encode()).hexdigest()
                                         ).first()

        if password is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        token_user = create_access_token(identity=usuario_auth.id)
        expireAt = datetime.now() + timedelta(minutes=30)
        usuario_auth.expireAt = expireAt
        usuario_auth.token = token_user
        commit()
        return {"id": usuario_auth.id,
                "token": token_user,
                "expireAt": expireAt.isoformat()}, 200

    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400