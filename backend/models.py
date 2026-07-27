from pydantic import BaseModel, Field, field_validator
import re
from datetime import date


class ChatRequest(BaseModel):
    session_id: str = Field(
        min_length=1,
        max_length=100
    )

    message: str = Field(
        min_length=1,
        max_length=1000
    )

    @field_validator("session_id", "message")
    @classmethod
    def validate_text(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty")

        return value


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]


class AppointmentRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    phone: str = Field(
        min_length=8,
        max_length=20
    )

    date: str

    time: str

    reason: str = Field(
        min_length=2,
        max_length=500
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        value = value.strip()

        if not re.match(
            r"^[A-Za-zÀ-ÿ\s'-]+$",
            value
        ):
            raise ValueError(
                "Name contains invalid characters"
            )

        return value


    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):

        value = value.strip()

        # Allow international and local phone formats
        if not re.match(
            r"^\+?[0-9\s\-()]{8,20}$",
            value
        ):
            raise ValueError(
                "Invalid phone number"
            )

        return value


    @field_validator("date")
    @classmethod
    def validate_date(cls, value):

        try:
            appointment_date = date.fromisoformat(
                value
            )

        except ValueError:
            raise ValueError(
                "Date must be in YYYY-MM-DD format"
            )

        if appointment_date < date.today():

            raise ValueError(
                "Appointment date cannot be in the past"
            )

        return value


    @field_validator("time")
    @classmethod
    def validate_time(cls, value):

        if not re.match(
            r"^(?:[01]\d|2[0-3]):[0-5]\d$",
            value
        ):
            raise ValueError(
                "Time must be in HH:MM format"
            )

        return value


class AppointmentResponse(BaseModel):
    message: str