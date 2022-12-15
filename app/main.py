from fastapi import FastAPI
from app.core.config import get_app_settings
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
# from app.core.events import create_start_app_handler, create_stop_app_handler

def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    ## Will open when use DB
    # application.add_event_handler(
    #     "startup",
    #     create_start_app_handler(application, settings),
    # )
    # application.add_event_Phandler(
    #     "shutdown",
    #     create_stop_app_handler(application)
    # )

    application.include_router(api_router, prefix=settings.api_prefix)

    return application

app = get_application()