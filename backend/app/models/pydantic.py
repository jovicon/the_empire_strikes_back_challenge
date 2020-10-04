from pydantic import BaseModel


class CrewPayloadSchema(BaseModel):
    name: str
    crew_quantity: int
    ship_name: str
    ship_cost: int
    ship_max_speed: int


class CrewResponseSchema(CrewPayloadSchema):
    id: int
