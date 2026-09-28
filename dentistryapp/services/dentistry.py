from collections.abc import Iterable
from dentistryapp.parameters import Parameters
from dentistryapp.models.appointment import DentistAppointment
from dentistryapp.models.appointment_configs import AppointmentConfig
from dentistryapp.models.patient import Patient


class DentalPractice:
    """Reglas de negocio del consultorio odontológico."""

    SETTINGS = {
        (Parameters.PARTICULAR, Parameters.LIMPIEZA): AppointmentConfig(
            Parameters.PARTICULAR, Parameters.LIMPIEZA, 80_000, 60_000
            ),
        (Parameters.PARTICULAR, Parameters.CALZA): AppointmentConfig(
            Parameters.PARTICULAR, Parameters.CALZA, 80_000, 80_000
        ),
        (Parameters.PARTICULAR, Parameters.EXTRACCION): AppointmentConfig(
            Parameters.PARTICULAR, Parameters.EXTRACCION, 80_000, 100_000
        ),
        (Parameters.PARTICULAR, Parameters.DIAGNOSTICO): AppointmentConfig(
            Parameters.PARTICULAR, Parameters.DIAGNOSTICO, 80_000, 50_000
        ),
        (Parameters.EPS, Parameters.LIMPIEZA): AppointmentConfig(
            Parameters.EPS, Parameters.LIMPIEZA, 5_000, 0
        ),
        (Parameters.EPS, Parameters.CALZA): AppointmentConfig(
            Parameters.EPS, Parameters.CALZA, 5_000, 40_000
        ),
        (Parameters.EPS, Parameters.EXTRACCION): AppointmentConfig(
            Parameters.EPS, Parameters.EXTRACCION, 5_000, 40_000
        ),
        (Parameters.EPS, Parameters.DIAGNOSTICO): AppointmentConfig(
            Parameters.EPS, Parameters.DIAGNOSTICO, 5_000, 0
        ),
        (Parameters.PREPAGADA, Parameters.LIMPIEZA): AppointmentConfig(
            Parameters.PREPAGADA, Parameters.LIMPIEZA, 30_000, 0
        ),
        (Parameters.PREPAGADA, Parameters.CALZA): AppointmentConfig(
            Parameters.PREPAGADA, Parameters.CALZA, 30_000, 10_000
        ),
        (Parameters.PREPAGADA, Parameters.EXTRACCION): AppointmentConfig(
            Parameters.PREPAGADA, Parameters.EXTRACCION, 30_000, 10_000
        ),
        (Parameters.PREPAGADA, Parameters.DIAGNOSTICO): AppointmentConfig(
            Parameters.PREPAGADA, Parameters.DIAGNOSTICO, 30_000, 0
        ),
    }

    @classmethod
    def get_value_by_client_type_attention_type(
        cls, client_type: str, attention_type: str, quantity: int
    ) -> int:
        setting = cls.SETTINGS.get((client_type, attention_type))
        if setting is None:
            raise ValueError(
                f"No existe una configuración para {client_type} / {attention_type}."
            )
        return setting.appointment_value + setting.attention_value * quantity

    @classmethod
    def calculate_appointment_value(cls, patient: Patient) -> int:
        return sum(
            cls.get_value_by_client_type_attention_type(
                patient.client_type,
                appointment.attention_type,
                appointment.quantity,
            )
            for appointment in patient.medical_appointments
        )

    @classmethod
    def create_appointment(
        cls,
        patient: Patient,
        attention_type: str,
        quantity: int,
        attention_priority: str,
        date: str,
    ) -> DentistAppointment:
        if attention_type not in Parameters.ATTENTION_TYPES:
            raise ValueError(f"Tipo de atención inválido: {attention_type}")

        if not cls.validate_quantity(attention_type, quantity):
            raise ValueError(
                f"Cantidad inválida para el tipo de atención {attention_type}: {quantity}"
            )

        if attention_priority not in Parameters.ATTENTION_PRIORITY:
            raise ValueError(f"Prioridad de atención inválida: {attention_priority}")

        if (patient.client_type, attention_type) not in cls.SETTINGS:
            raise ValueError(
                f"No existe una configuración para {patient.client_type} / {attention_type}."
            )

        appointment = DentistAppointment(
            attention_type=attention_type,
            quantity=quantity,
            attention_priority=attention_priority,
            date=date,
        )
        patient.medical_appointments.append(appointment)
        return appointment

    @staticmethod
    def validate_quantity(attention_type: str, quantity: int) -> bool:
        if not isinstance(quantity, int) or quantity <= 0:
            return False
        if attention_type in Parameters.SINGLE_QUANTITY_ATTENTION_TYPES:
            return quantity == 1
        return True

    @classmethod
    def sort_patients_by_date(cls, patients: Iterable[Patient]) -> list[Patient]:
        return sorted(patients, key=cls._earliest_date)

    @classmethod
    def sort_patients_by_total_value(cls, patients: Iterable[Patient]) -> list[Patient]:
        return sorted(
            patients,
            key=cls.calculate_appointment_value,
            reverse=True,
        )

    @classmethod
    def total_revenue(cls, patients: Iterable[Patient]) -> int:
        return sum(cls.calculate_appointment_value(patient) for patient in patients)

    @staticmethod
    def patients_by_attention_type(
        patients: Iterable[Patient], attention_type: str
    ) -> int:
        return sum(
            1
            for patient in patients
            if any(
                appointment.attention_type == attention_type
                for appointment in patient.medical_appointments
            )
        )

    @staticmethod
    def _earliest_date(patient: Patient) -> str:
        dates = [appointment.date for appointment in patient.medical_appointments]
        return min(dates) if dates else "2262-12-31 23:59"
