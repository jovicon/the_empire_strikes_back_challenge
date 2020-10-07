from typing import List

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import (
    CrewPayloadSchema,
    CrewResponseSchema,
    CrewUpdatePayloadSchema,
)
from app.models.tortoise import CrewSchema

router = APIRouter()

# TODO:
# Create a Crew - Ready
# Read all Crews - Almost ready - paginating missing
# Update a Crew (dado un ID)
# Delete a Crew (dado un ID)


@router.post("/", response_model=CrewResponseSchema, status_code=201)
async def create_crew(payload: CrewPayloadSchema) -> CrewResponseSchema:
    """
    Create a Crew.

    Crea una tripulación, se guarda la siguiente informacion:

    * ID de la tripulación
    * Nombre de la tripulación
    * Cantidad de tripulantes
    * Modelo de la nave espacial
    * Costo de la nave espacial
    * Velocidad máxima de la nave espacial

    """
    crew_id = await crud.post(payload)

    response_object = {
        "id": crew_id,
        "name": payload.name,
        "crew_quantity": payload.crew_quantity,
        "ship_name": payload.ship_name,
        "ship_cost": payload.ship_cost,
        "ship_max_speed": payload.ship_max_speed,
    }

    return response_object


@router.get("/{id}/", response_model=CrewSchema)
async def read_crew(id: int) -> CrewSchema:
    crew = await crud.get(id)
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")

    return crew


@router.get("/", response_model=List[CrewSchema])
async def read_all_crews() -> List[CrewSchema]:
    """
    Read all Crews

    * Deberás crear una paginación para este endpoint
    * Se podrá buscar por nombre de tripulación
    * Obtener una tripulación con la información detallada (dado un ID)
    """
    return await crud.get_all()


@router.delete("/{id}/", response_model=CrewResponseSchema)
async def delete_crew(id: int) -> CrewResponseSchema:
    crew = await crud.get(id)
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")

    await crud.delete(id)

    return crew


@router.put("/{id}/", response_model=CrewSchema)
async def update_crew(id: int, payload: CrewUpdatePayloadSchema) -> CrewSchema:
    crew = await crud.put(id, payload)
    if not crew:
        raise HTTPException(status_code=404, detail="Crew not found")

    return crew
