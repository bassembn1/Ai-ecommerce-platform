import time
import uuid

from fastapi import Request

from app.core.logging import logger


async def log_requests(
    request: Request,
    call_next,
):

    request_id = str(uuid.uuid4())

    start_time = time.time()

    response = await call_next(request)

    process_time = (
        time.time() - start_time
    )

    response.headers["X-Request-ID"] = request_id

    logger.info(
        f"""
        Request ID: {request_id}
        Method: {request.method}
        Path: {request.url.path}
        Status: {response.status_code}
        Time: {process_time:.4f}s
        """
    )

    return response