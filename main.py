from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from dependencies import get_query_token, get_token_header
from routers import items, users, admin, background_task, send_email

description = """
Demo Fast API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

# app = FastAPI(
#     title="Demo Fast epi",
#     description=description,
#     version="0.0.1",
#     terms_of_service="http://example.com/terms/",
#     contact={
#         "name": "Deadpoolio the Amazing",
#         "url": "http://x-force.example.com/contact/",
#         "email": "dp@x-force.example.com",
#     },
#     license_info={
#         "name": "Apache 2.0",
#         "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
#     },
# )

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

# app = FastAPI(openapi_tags=tags_metadata)

app = FastAPI(openapi_url="/api/v1/openapi.json")



app.include_router(users.router)
app.include_router(items.router)
app.include_router(background_task.router)
app.include_router(send_email.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}