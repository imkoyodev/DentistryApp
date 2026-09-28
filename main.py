from dentistryapp.cli import input_handler
from dentistryapp.cli.menu import print_menu, print_table
from dentistryapp.parameters import Parameters
from dentistryapp.data_repository.repository import PatientRepository
from dentistryapp.test.synt_data import synthetic_records
from dentistryapp.services.dentistry import DentalPractice


class DentalPracticeCLI:
    """Casos de Uso para CLI del Aplicativo"""

    def __init__(
        self,
        repository: PatientRepository,
        practice: DentalPractice,
    ) -> None:
        self.repository = repository
        self.practice = practice

    @staticmethod
    def _was_cancelled(value: object) -> bool:
        if value is None:
            print("Operación cancelada. Volviendo al menú principal.")
            return True
        return False

    def run(self) -> None:
        while True:
            option = print_menu()

            actions = {
                "1": self.add_patient,
                "2": self.find_patient,
                "3": self.assign_appointment,
                "4": self.show_patient_appointments,
                "5": self.show_patients_by_value,
                "6": self.show_total_revenue,
                "7": self.show_extraction_count,
                "8": self.show_patient_count,
                "9": self.search_in_sorted_patients,
                "10": self.show_patients_by_date,
                "11": self.exit,
            }

            if actions[option]():
                return

    def add_patient(self) -> bool:
        patient_id = input_handler.read_valid_ID()
        if self._was_cancelled(patient_id):
            return False

        if self.repository.get_by_id(patient_id):
            patient = self.repository.get_by_id(patient_id)
            print(
                f"El Paciente {patient.name} ya existe en el registro"
                f"(ID: {patient.id_patient}, teléfono: {patient.phone}, "
                f"tipo de cliente: {patient.client_type})"
            )
            return False

        try:
            name = input_handler.read_valid_name()
            if self._was_cancelled(name):
                return False

            phone = input_handler.read_valid_phone()
            if self._was_cancelled(phone):
                return False

            client_type = input_handler.read_valid_choice(
                "Ingrese el tipo de cliente",
                Parameters.CLIENT_TYPES,
            )
            if self._was_cancelled(client_type):
                return False

            from dentistryapp.models.patient import Patient

            patient = Patient(patient_id, name, phone, client_type)
            self.repository.add(patient)
            print(f"Paciente {patient.name} agregado exitosamente.")
        except ValueError as error:
            print(f"No se pudo agregar el paciente: {error}")

        return False

    def find_patient(self) -> bool:
        patient_id = input_handler.read_valid_ID()
        if self._was_cancelled(patient_id):
            return False

        patient = self.repository.get_by_id(patient_id)
        if patient:
            print(
                f"Nombre: {patient.name} con cédula número: {patient.id_patient} "
                f"teléfono: {patient.phone} tipo de cliente: {patient.client_type}"
            )
        else:
            print(f"Paciente no encontrado: {patient_id}")
        return False

    def assign_appointment(self) -> bool:
        patient_id = input_handler.read_valid_ID()
        if self._was_cancelled(patient_id):
            return False

        patient = self.repository.get_by_id(patient_id)
        if not patient:
            print(f"Paciente no encontrado: {patient_id}")
            return False

        attention_type = input_handler.read_valid_choice(
            "Tipo de Atención",
            Parameters.ATTENTION_TYPES,
        )
        if self._was_cancelled(attention_type):
            return False

        quantity = input_handler.read_valid_quantity(attention_type)
        if self._was_cancelled(quantity):
            return False

        priority = input_handler.read_valid_choice(
            "Prioridad del Servicio",
            Parameters.ATTENTION_PRIORITY,
        )
        if self._was_cancelled(priority):
            return False

        date = input_handler.read_valid_date()
        if self._was_cancelled(date):
            return False

        try:
            self.practice.create_appointment(
                patient,
                attention_type,
                quantity,
                priority,
                date,
            )
            total = self.practice.get_value_by_client_type_attention_type(
                patient.client_type,
                attention_type,
                quantity,
            )
            print(
                "Asignación de Cita Exitosa. "
                f"Valor Adeudado por Servicio: {total}"
            )
        except ValueError as error:
            print(f"Cita no asignada: {error}")

        return False

    def show_patient_appointments(self) -> bool:
        patient_id = input_handler.read_valid_ID()
        if self._was_cancelled(patient_id):
            return False

        patient = self.repository.get_by_id(patient_id)
        if not patient:
            print(f"Paciente no encontrado: {patient_id}")
            return False

        total = self.practice.calculate_appointment_value(patient)
        print(
            f"Paciente {patient.name} con {len(patient.medical_appointments)} "
            f"citas asignadas por un valor total a pagar de {total}"
        )

        rows = [
            (
                appointment.attention_type,
                appointment.date,
                str(appointment.quantity),
                appointment.attention_priority,
                str(
                    self.practice.get_value_by_client_type_attention_type(
                        patient.client_type,
                        appointment.attention_type,
                        appointment.quantity,
                    )
                ),
            )
            for appointment in patient.medical_appointments
        ]

        print_table(
            ("Tipo de atención", "Fecha", "Cantidad", "Prioridad", "Valor"),
            rows,
        )
        return False

    def show_patients_by_value(self) -> bool:
        patients = self.practice.sort_patients_by_total_value(
            self.repository.all()
        )
        rows = [
            (
                patient.name,
                str(patient.id_patient),
                str(self.practice.calculate_appointment_value(patient)),
            )
            for patient in patients
        ]
        print_table(("Nombre", "Cédula", "Valor total"), rows)
        return False

    def show_total_revenue(self) -> bool:
        total = self.practice.total_revenue(self.repository.all())
        print(f"Ingresos Totales: {total}")
        return False

    def show_extraction_count(self) -> bool:
        count = self.practice.patients_by_attention_type(
            self.repository.all(),
            Parameters.EXTRACCION,
        )
        print(f"Total de pacientes servicio de exodoncia: {count}")
        return False

    def show_patient_count(self) -> bool:
        print(f"Clientes Totales: {self.repository.count()}")
        return False

    def search_in_sorted_patients(self) -> bool:
        patients = self.practice.sort_patients_by_total_value(
            self.repository.all()
        )
        print("=== Valores Adeudados Por Cliente ===")

        rows = [(patient.name, str(patient.id_patient)) for patient in patients]
        print_table(("Nombre", "Cédula"), rows)

        patient_id = input_handler.read_valid_ID(
            "Ingrese Documento de Identidad Solicitado: "
        )
        if self._was_cancelled(patient_id):
            return False

        patient = next(
            (candidate for candidate in patients if candidate.id_patient == patient_id),
            None,
        )

        if patient:
            position = patients.index(patient) + 1
            total = self.practice.calculate_appointment_value(patient)
            print(
                f"Identificado en {position} de {len(patients)}: "
                f"Nombre: {patient.name} valor total: {total}"
            )
        else:
            print(f"Paciente no encontrado: {patient_id}")

        return False

    def show_patients_by_date(self) -> bool:
        patients = [
            patient
            for patient in self.repository.all()
            if patient.medical_appointments
        ]
        patients = self.practice.sort_patients_by_date(patients)

        rows = []
        for patient in patients:
            appointments = sorted(
                patient.medical_appointments,
                key=lambda appointment: appointment.date,
            )
            rows.extend(
                (
                    patient.name,
                    str(patient.id_patient),
                    appointment.attention_type,
                    appointment.date,
                    str(appointment.quantity),
                    appointment.attention_priority,
                )
                for appointment in appointments
            )

        print_table(
            ("Nombre", "Cédula", "Tipo de atención", "Fecha", "Cantidad", "Prioridad"),
            rows,
        )
        return False

    @staticmethod
    def exit() -> bool:
        print("Cerrando ...")
        return True


def main() -> None:
    repository = PatientRepository(synthetic_records())
    practice = DentalPractice()
    DentalPracticeCLI(repository, practice).run()


if __name__ == "__main__":
    main()
