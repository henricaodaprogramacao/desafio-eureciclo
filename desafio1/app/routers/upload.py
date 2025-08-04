from fastapi import APIRouter, UploadFile, File
from desafio1.app.services.extract import extract_zip, parse_xml
from desafio1.app.services.amqp import publish_message
from desafio1.app.services.storage import save_file
from desafio1.app.routers.publications import publications_data

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    file_path = save_file(file_bytes, file.filename)

    extracted_files = extract_zip(file_path)
    publications = [parse_xml(f) for f in extracted_files]

    for pub in publications:
        publications_data.append(pub)
        publish_message(pub.dict())

    return {"message": f"{len(publications)} publicações extraídas e enviadas para AMQP"}
