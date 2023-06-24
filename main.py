"""This is the main module to start the service
This module defines below usecases:
1) Configures logger
4) Creates multiple middlewares
5) Api versioning
6) Including routers
"""

__version__ = "v1.0"
__author__ = "rajesh@twiq.club"

import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# from fastapi.middleware.gzip import GZipMiddleware
# from app.middlewares.contextmiddleware import RequestContextMiddleware
from app.utilities import twiq_logger
from app.routers import v1_router
import uvicorn

logger = twiq_logger.TwiqLogger(
    twiq_logger.get_logger(__name__), {"model_inference": "v1"}
)

app = FastAPI()
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
# app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.add_middleware(RequestContextMiddleware)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Process Time: " + str(process_time))
    return response

@app.get("/")
async def healthcheck():
    return {"status": "alive"}


subapi_v1 = FastAPI()
# subapi_v2 =  FastAPI()

subapi_v1.include_router(v1_router.router)
# subapi_v2.include_router(v2_router.router)

app.mount("/v1/model-inference", subapi_v1)

logger.info("Main application initialized")


if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=5002)
    # pass

