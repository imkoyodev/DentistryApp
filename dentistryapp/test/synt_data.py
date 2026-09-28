from collections import deque
from dentistryapp.parameters import Parameters
from dentistryapp.models.appointment import DentistAppointment
from dentistryapp.models.patient import Patient

def synthetic_records() -> deque[Patient]:
    return deque(
        [
            Patient(
                1234567891,
                "Andrés Felipe Martínez Gómez",
                "3000000001",
                Parameters.PARTICULAR,
                deque(
                    [
                        DentistAppointment(
                            Parameters.CALZA, 2, Parameters.PRIORITARIO, "2027-01-29 17:25"
                        )
                    ]
                ),
            ),
            Patient(
                1345678902,
                "Laura Daniela Rodríguez Pérez",
                "3000000002",
                Parameters.EPS,
                deque(
                    [
                        DentistAppointment(
                            Parameters.LIMPIEZA, 1, Parameters.REGULAR, "2026-10-05 08:30"
                        )
                    ]
                ),
            ),
            Patient(
                1456789013,
                "Carlos Eduardo Ramírez Torres",
                "3010000003",
                Parameters.PREPAGADA,
                deque(
                    [
                        DentistAppointment(
                            Parameters.DIAGNOSTICO, 1, Parameters.REGULAR, "2026-11-02 09:15"
                            )
                    ]
                ),
            ),
            Patient(
                1567890124,
                "Mariana Isabel González López",
                "3040000006",
                Parameters.PARTICULAR,
                deque(
                    [
                        DentistAppointment(
                           Parameters.EXTRACCION, 1, Parameters.PRIORITARIO, "2027-01-18 08:50"
                        )
                    ]
                ),
            ),
            Patient(
                1678901235,
                "Juan Sebastián Herrera Castro",
                "3020000004",
                Parameters.EPS,
                deque(
                    [
                        DentistAppointment(
                            Parameters.CALZA, 4, Parameters.PRIORITARIO, "2026-12-03 11:00"
                            
                        )
                    ]
                ),
            ),
            Patient(
                1789012346,
                "Valentina Sofía Moreno Díaz",
                "3050000007",
                Parameters.PREPAGADA,
                deque(
                    [
                        DentistAppointment(
                            Parameters.LIMPIEZA, 1, Parameters.REGULAR, "2026-12-14 13:30"
                        )
                    ]
                ),
            ),
            Patient(
                1890123457,
                "Diego Alejandro Vargas Ruiz",
                "3060000008",
                Parameters.PARTICULAR,
                deque(
                    [
                        DentistAppointment(
                            Parameters.EXTRACCION, 6, Parameters.PRIORITARIO, "2026-11-19 16:20"
                        )
                    ]
                ),
            ),
            Patient(
                1901234568,
                "Camila Andrea Sánchez Rojas",
                "3030000005",
                Parameters.EPS,
                deque(
                    [
                        DentistAppointment(
                            Parameters.LIMPIEZA, 1, Parameters.REGULAR, "2026-12-14 13:30"
                            
                        )
                    ]
                ),
            ),
            Patient(
                    1112345679,
                    "Paula Alejandra Cárdenas Mejía",
                    "3070000009",
                    Parameters.PREPAGADA,
                    deque(
                          [
                            DentistAppointment(
                                Parameters.DIAGNOSTICO, 1, Parameters.REGULAR, "2026-10-17 14:45"
                            
                            )
                          ]
                        ),
                    ),
            Patient(
                    1223456780,
                    "Nicolás Esteban Jiménez Restrepo",
                    "3080000010",
                    Parameters.EPS,
                    deque(
                       [
                         DentistAppointment(
                         Parameters.LIMPIEZA, 1, Parameters.REGULAR, "2027-01-07 15:10"
                         )
                       ]
                     ),
                 ),
        ]
    )




