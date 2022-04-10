import logging
from functools import lru_cache

import easyocr
import numpy as np
from fastapi import APIRouter, Depends, File, UploadFile
from PIL import Image

from app.models import DetectedTextResponse

log = logging.getLogger("uvicorn")

router = APIRouter()


@lru_cache()
def ocr_reader():
    log.info("Loading easyocr reader")
    ocr = easyocr.Reader(["en"], gpu=False)
    return ocr


@router.post("/ocr", response_model=DetectedTextResponse)
async def ocr_by_file(
    file: UploadFile = File(...), ocr: easyocr.Reader = Depends(ocr_reader)
):
    if file is None:
        raise Exception("No file provided for ocr")
    log.info("Reading Image File")
    raw_image = Image.open(file.file).convert("RGB")
    image = np.asarray(raw_image)

    log.info("Detecting Text")
    detections = ocr.readtext(image, output_format="dict")
    output = DetectedTextResponse.from_list(detections)
    log.info(output.detections[0] if len(output.detections) else output)
    return output
