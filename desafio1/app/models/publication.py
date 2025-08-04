from pydantic import BaseModel
from typing import Optional

class Publication(BaseModel):
    idOficio: Optional[str] = None
    pubName: Optional[str] = None
    artType: Optional[str] = None
    pubDate: Optional[str] = None
    artClass: Optional[str] = None
    artCategory: Optional[str] = None
    artSize: Optional[str] = None
    artNotes: Optional[str] = None
    numberPage: Optional[str] = None
    pdfPage: Optional[str] = None
    editionNumber: Optional[str] = None
    highlightType: Optional[str] = None
    highlightPriority: Optional[str] = None
    highlight: Optional[str] = None
    highlightimage: Optional[str] = None
    highlightimagename: Optional[str] = None
    idMateria: Optional[str] = None
    Identifica: Optional[str] = None
    Ementa: Optional[str] = None
    SubTitulo: Optional[str] = None
