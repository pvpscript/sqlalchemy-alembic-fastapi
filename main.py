import uvicorn

from fastapi import FastAPI, APIRouter, Response, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.platform import Platform, PlatformCreate, PlatformUpdate
from app.schemas.user_platform import UserPlatform, UserPlatformCreate
from app.schemas.document import Document, DocumentCreate, DocumentUpdate
from app.schemas.asset import Asset, AssetCreate, AssetUpdate

from app.db.services.user import UserService, get_user_service
from app.db.services.platform import PlatformService, get_platform_service
from app.db.services.user_platform_association import UserPlatformAssociationService, get_user_platform_association_service
from app.db.services.document import DocumentService, get_document_service
from app.db.services.asset import AssetService, get_asset_service

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



testing_router = APIRouter(prefix='/testing', tags=['testing'])

from pydantic import BaseModel
class UserPlatformsPayload(BaseModel):
    user: User
    platforms: List[Platform]

class PlatformUsersPayload(BaseModel):
    users: List[User]
    platform: Platform

class TestPayload(BaseModel):
    user: UserCreate
    platform: PlatformCreate
    document: DocumentCreate
    assets: List[AssetCreate]

@testing_router.post("/")
async def test(payload: TestPayload,
               user_service: UserService = Depends(get_user_service),
               platform_service: PlatformService = Depends(get_platform_service),
               user_platform_association_service: UserPlatformAssociationService = Depends(get_user_platform_association_service),
               document_service: DocumentService = Depends(get_document_service),
               asset_service: AssetService = Depends(get_asset_service)):
    user = await user_service.save(payload.user)
    print("----------------------------------------------------------------------------------------------------")
    print(user)
    print("----------------------------------------------------------------------------------------------------")
    platform = await platform_service.save(payload.platform)
    print("----------------------------------------------------------------------------------------------------")
    print(platform)
    print("----------------------------------------------------------------------------------------------------")

    user_platform_create = UserPlatformCreate(user_id=user.id,
                                              platform_id=platform.id)
    user_platform = await user_platform_association_service.save(user_platform_create)
    print("----------------------------------------------------------------------------------------------------")
    print(user_platform)
    print("----------------------------------------------------------------------------------------------------")

    updated_document = payload.document.copy(update={'user_id': user.id})
    document = await document_service.save(updated_document)
    print("----------------------------------------------------------------------------------------------------")
    print(document)
    print("----------------------------------------------------------------------------------------------------")
    for payload_asset in payload.assets:
        updated_asset = payload_asset.copy(update={'user_id': user.id})
        asset = await asset_service.save(updated_asset)
        print("----------------------------------------------------------------------------------------------------")
        print(asset)
        print("----------------------------------------------------------------------------------------------------")

    result_user = await user_service.get_by_id(user.id)
    print("----------------------------------------------------------------------------------------------------")
    print(result_user)


    



app = FastAPI()

app.include_router(user_router)
app.include_router(platform_router)
app.include_router(testing_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
        host="0.0.0.0",
        port=8082,
    )
