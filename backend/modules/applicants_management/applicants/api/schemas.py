from modules.applicants_management.applicants.models.applicant import Applicant
from ninja import ModelSchema, Schema

# --- SCHEMAS ---

class ApplicantSchema(ModelSchema):
    """
    Esquema para representar un solicitante en las respuestas de la API.
    """
    class Meta:
        model = Applicant
        fields = ['id', 'name', 'email', 'age', 'created_at', 'updated_at']

class ApplicantCreateSchema(Schema):
    """
    Esquema para crear un nuevo solicitante.
    """
    name: str
    email: str
    age: int