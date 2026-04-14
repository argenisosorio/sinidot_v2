from modules.donors_management.donors.models.donor import Donor
from ninja import ModelSchema, Schema

# --- SCHEMAS ---

class DonorSchema(ModelSchema):
    """
    XXXXXXXXXXXXXXXX
    """
    class Meta:
        model = Donor
        fields = ['id', 'name', 'email', 'age', 'created_at', 'updated_at']

class DonorCreateSchema(Schema):
    """
    XXXXXXXXXXXXXXXXXXXX
    """
    name: str
    email: str
    age: int
