from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class AppointmentConfig:
    """
    Define los dtypes de las variables de una consulta
    """
    client_type: str
    attention_type: str
    appointment_value: int
    attention_value: int