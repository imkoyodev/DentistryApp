from collections import deque
from dataclasses import dataclass, field

from .appointment import DentistAppointment


@dataclass(slots=True)

class Patient:
    id_patient: int
    name: str
    phone: str
    client_type: str
    medical_appointments: deque[DentistAppointment] = field(default_factory=deque)