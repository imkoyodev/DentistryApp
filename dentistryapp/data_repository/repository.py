from collections import deque
from dentistryapp.models.patient import Patient


class PatientRepository:
    """
    Almacenamiento en memoria de los registros de pacientes
    """

    def __init__(self, patients: deque[Patient] | None = None) -> None:
        self._patients = patients if patients is not None else deque()

    def add(self, patient: Patient) -> None:
        if self.get_by_id(patient.id_patient) is not None:
            raise ValueError(f"El paciente ya existe: {patient.id_patient}")
        self._patients.append(patient)

    def get_by_id(self, patient_id: int) -> Patient | None:
        return next(
            (patient for patient in self._patients if patient.id_patient == patient_id),
            None,
        )

    def all(self) -> list[Patient]:
        return list(self._patients)

    def count(self) -> int:
        return len(self._patients)
