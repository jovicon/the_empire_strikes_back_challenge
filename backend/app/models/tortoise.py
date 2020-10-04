from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Crew(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    crew_quantity = fields.IntField()

    ship_name = fields.CharField(max_length=255)
    ship_cost = fields.IntField()
    ship_max_speed = fields.IntField()

    datetime = fields.DatetimeField(null=True)

    def __str__(self):
        crew = [
            self.id,
            self.name,
            self.crew_quantity,
            self.ship_name,
            self.ship_cost,
            self.ship_max_speed,
        ]
        return "Crew: " + " ".join(crew)


CrewSchema = pydantic_model_creator(Crew)
