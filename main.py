import uvicorn

from fastapi import FastAPI, APIRouter, Response, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.platform import Platform, PlatformCreate, PlatformUpdate

from app.db.services.user import UserService, get_user_service
from app.db.services.platform import PlatformService, get_platform_service

from typing import List
from uuid import UUID


user_router = APIRouter(prefix='/user', tags=['user'])

@user_router.get("/", response_model=List[User])
async def read(user_service: UserService = Depends(get_user_service)) -> Response:
    res = await user_service.list()

    return res

@user_router.post("/")
async def create(payload: UserCreate, user_service: UserService = Depends(get_user_service)) -> Response:
    res = await user_service.save(payload)

    return res

@user_router.put("/{user_id}")
async def update(user_id: UUID, payload: UserUpdate, user_service: UserService = Depends(get_user_service)) -> Response:
    res = await user_service.update(user_id, payload)

    return res

@user_router.delete("/{user_id}")
async def delete(user_id: UUID, user_service: UserService = Depends(get_user_service)) -> Response:
    res = await user_service.delete(user_id)

    return res


platform_router = APIRouter(prefix='/platform', tags=['platform'])

@platform_router.get("/", response_model=List[Platform])
async def read(platform_service: PlatformService = Depends(get_platform_service)) -> Response:
    res = await platform_service.list()

    return res

@platform_router.post("/")
async def create(payload: PlatformCreate, platform_service: PlatformService = Depends(get_platform_service)) -> Response:
    res = await user_service.save(payload)

    return res

@platform_router.put("/{platform_id}")
async def update(platform_id: UUID, payload: PlatformUpdate, platform_service: PlatformService = Depends(get_platform_service)) -> Response:
    res = await platorm_service.update(platform_id, payload)

    return res

@platform_router.delete("/{platform_id}")
async def delete(platform_id: UUID, platform_service: PlatformService = Depends(get_platform_service)) -> Response:
    res = await platform_service.delete(platform_id)

    return res



app = FastAPI()

app.include_router(user_router)
app.include_router(platform_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
        host="0.0.0.0",
        port=8082,
    )
