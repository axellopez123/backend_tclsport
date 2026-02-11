from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.auth.schemas.auth import UserCreate, Token, UserOut, UserUpdate
from app.auth.core.utils import hash_password, verify_password, create_access_token
from app.database import get_db
from app.auth.models.user import UserDB, UserRole
from app.auth.core.dependencies import get_current_user
from sqlalchemy.orm import selectinload
from fastapi.responses import JSONResponse
from sqlalchemy import or_
from typing import List


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserDB).where(UserDB.username == user.username))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    new_user = UserDB(username=user.username, hashed_password=hash_password(user.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    token = create_access_token({"sub": new_user.username})
    # return {"access_token": token, "token_type": "bearer"}
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=True,       # Requiere HTTPS en producción
        samesite="None",    # O "Strict" si no tienes frontend externo
        max_age=1800,      # 30 minutos o lo que decidas
        path="/"
    )
    return response