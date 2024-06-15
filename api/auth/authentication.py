import jwt
from datetime import datetime, timedelta
from django.conf import settings
from api.models import User
from api.repository.repository import Repository


def authenticate(email, password):
    repository = Repository(User, 'users')
    user = repository.get_user_by_email_and_password(email, password)
    return user

def generateToken(user_id, email):
    payload = {
        "id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=5),
    }
    return jwt.encode(
        payload=payload, key=getattr(settings, "SECRET_KEY"), algorithm="HS256"
    )

def refreshToken(user):
    return generateToken(user)

def verifyToken(token):
    error_code = 0
    payload = None
    try:
        payload = jwt.decode(jwt=token,
                      key=getattr(settings, "SECRET_KEY"),
                      algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        error_code = 1
    except jwt.InvalidTokenError:
        error_code = 2

    return [error_code, payload]

def getAuthenticatedUser(token):
    _, payload = verifyToken(token)

    if payload is not None:
        # recuperar o usuario no banco
        return User(email=payload['email'])