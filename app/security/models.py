# File app/security/models.py

from pydantic import BaseModel

class ApiKeyResponse(BaseModel):
    message: str
    client: str | None = None
    status: str