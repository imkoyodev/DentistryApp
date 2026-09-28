from dataclasses import dataclass

@dataclass(slots=True)
class DentistAppointment:
    """
    Define los dtypes de las variables de una consulta
    """
    attention_type: str
    quantity: int
    attention_priority: str
    date: str