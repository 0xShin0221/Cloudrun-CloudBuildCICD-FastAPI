from fastapi import FastAPI
import uvicorn
import signal
import sys
from types import FrameType

from utils.logging import logger, flush

app = FastAPI()

@app.get("/")
async def hello():
    logger.info(logField="custom-entry", arbitraryField="custom-entry")
    logger.info("Child logger with trace Id.")
    return {"message": "Hello, World!"}

def shutdown_handler(signal_int: int, frame: FrameType) -> None:
    logger.info(f"Caught Signal {signal.strsignal(signal_int)}")
    flush()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)
    uvicorn.run(app, host="localhost", port=8080, log_level="debug")
