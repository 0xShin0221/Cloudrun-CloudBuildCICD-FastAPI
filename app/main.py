from logging import getLogger
from typing import Dict

from fastapi import FastAPI

import uvicorn

logger = getLogger("uvicorn.app")
app = FastAPI()


@app.get("/", tags=["root"])
async def root() -> Dict[str, str]:
    return {"message": "Cloud build setup complete!"}


if __name__ == "__main__":
    logger.info("Starting server")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
