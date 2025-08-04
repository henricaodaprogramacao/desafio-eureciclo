from fastapi import APIRouter
from typing import List
from desafio1.app.models.publication import Publication

publications_data: List[Publication] = []

router = APIRouter(prefix="/publications", tags=["Publications"])

@router.get("/", response_model=List[Publication])
def list_publications():
    return publications_data
