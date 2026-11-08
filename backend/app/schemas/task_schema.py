from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Literal


class createTaskSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=1)
    description: str = ""

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Title cannot be empty")

        return value

class UpdateTaskSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(default=None, min_length=1)
    description: str | None = None
    status: Literal["pending", "in_progress", "completed"] | None = None
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if value is not None:
            value = value.strip()

            if not value:
                raise ValueError("Title cannot be empty")

        return value            