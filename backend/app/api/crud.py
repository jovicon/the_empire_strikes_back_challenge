from typing import Union, List

from app.models.pydantic import CrewPayloadSchema
from app.models.tortoise import Crew


async def post(payload: CrewPayloadSchema) -> int:
    crew = Crew(
        name=payload.name,
        crew_quantity=payload.crew_quantity,
        ship_name=payload.ship_name,
        ship_cost=payload.ship_cost,
        ship_max_speed=payload.ship_max_speed,
    )
    await crew.save()
    return crew.id


async def get(id: int) -> Union[dict, None]:
    crew = await Crew.filter(id=id).first().values()
    if crew:
        return crew[0]
    return None


async def get_all() -> List:
    crews = await Crew.all().values()
    return crews
