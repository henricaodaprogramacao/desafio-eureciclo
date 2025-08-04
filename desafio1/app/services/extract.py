import os
import zipfile
import xml.etree.ElementTree as ET
from desafio1.app.models.publication import Publication
from desafio1.app.config import UPLOAD_DIR

def extract_zip(file_path: str):
    extracted_files = []
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        extract_path = os.path.join(UPLOAD_DIR, "extracted")
        os.makedirs(extract_path, exist_ok=True)
        zip_ref.extractall(extract_path)
        extracted_files = [
            os.path.join(extract_path, f) for f in zip_ref.namelist() if f.endswith(".xml")
        ]
    return extracted_files

import xml.etree.ElementTree as ET

def parse_xml(file_path: str) -> Publication:
    tree = ET.parse(file_path)
    root = tree.getroot()
    article = root.find(".//article")  # pega o elemento <article>

    return Publication(
        idOficio=article.get("idOficio"),
        pubName=article.get("pubName"),
        artType=article.get("artType"),
        pubDate=article.get("pubDate"),
        artClass=article.get("artClass"),
        artCategory=article.get("artCategory"),
        artSize=article.get("artSize"),
        artNotes=article.get("artNotes"),
        numberPage=article.get("numberPage"),
        pdfPage=article.get("pdfPage"),
        editionNumber=article.get("editionNumber"),
        highlightType=article.get("highlightType"),
        highlightPriority=article.get("highlightPriority"),
        highlight=article.get("highlight"),
        highlightimage=article.get("highlightimage"),
        highlightimagename=article.get("highlightimagename"),
        idMateria=article.get("idMateria"),
        Identifica=article.findtext(".//Identifica"),
        Ementa=article.findtext(".//Ementa"),
        SubTitulo=article.findtext(".//SubTitulo")
    )
