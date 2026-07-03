from pydantic import BaseModel,computed_field, Field
from typing import Annotated, Literal
from config.region_tier import south,north

south=["southeast", "southwest"]
north=["northeast", "northwest"]

class InputData(BaseModel):
    age: Annotated[int, Field(ge=0, le=120, description="Age of the individual in years")]
    sex: Annotated[Literal["male", "female"], Field(description="Sex of the individual")]
    bmi: Annotated[float, Field(ge=0, description="Body mass index")]
    children: Annotated[int, Field(ge=0, description="Number of children")]
    smoker: Annotated[Literal["yes", "no"], Field(description="Whether the individual is a smoker")]
    region: Annotated[Literal["northeast", "northwest", "southeast", "southwest"], Field(description="Region of the individual")]

    @computed_field
    @property
    def bmi_category(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
    @computed_field
    @property
    def age_category(self) -> str:
        if self.age < 18:
            return "under age"
        elif 18 <= self.age < 35:
            return "best age"
        else:
            return "over_age"
    @computed_field
    @property
    def region_category(self) -> str:
        if self.region in south:
            return "south"
        else:
            return "north" 