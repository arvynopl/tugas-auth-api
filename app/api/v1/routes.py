# File app/api/v1/routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.security.auth import (
    Token, UserLogin, authenticate_user,
    verify_api_key
)

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(user_login: UserLogin):
    user = authenticate_user(user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return Token(
        access_token="dummy-jwt-token",
        token_type="bearer",
        api_key=user["api_key"]
    )

@router.get("/secure")
async def secure_route(user: dict = Depends(verify_api_key)):
    return {
        "message": "Access granted to secure endpoint",
        "username": user["username"]
    }

@router.get("/public")
async def public_route():
    return {
        "message": "This is a public endpoint"
    }