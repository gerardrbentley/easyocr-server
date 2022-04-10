from typing import List

from pydantic import BaseModel


class Coordinate(BaseModel):
    x: int
    y: int


class BoundingBox(BaseModel):
    top_left: Coordinate
    top_right: Coordinate
    bottom_right: Coordinate
    bottom_left: Coordinate


corners = ("top_left", "top_right", "bottom_right", "bottom_left")


class DetectedText(BaseModel):
    bounding_box: BoundingBox
    text: str
    confidence: float

    @classmethod
    def from_dict(cls, ocr_result: dict):
        coords = {
            name: Coordinate(x=x, y=y)
            for name, (x, y) in zip(corners, ocr_result["boxes"])
        }
        box = BoundingBox(**coords)
        return cls(
            bounding_box=box,
            text=ocr_result["text"],
            confidence=ocr_result["confident"],
        )


class DetectedTextResponse(BaseModel):
    detections: List[DetectedText]

    @classmethod
    def from_list(cls, ocr_list_result: list[dict]):
        detections = [DetectedText.from_dict(x) for x in ocr_list_result]
        return cls(detections=detections)
