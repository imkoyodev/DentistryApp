from collections.abc import Sequence


OPTIONS = (
    "1. Nuevo Paciente",
    "2. Busqueda por identificación",
    "3. Asignación de Cita",
    "4. Historico de Citas",
    "5. Cuentas por Cobrar",
    "6. Ingresos Totales",
    "7. Total de Extracciones Dentales",
    "8. Total de Pacientes",
    "9. Ordenar clientes por valor y buscar uno por cédula",
    "10. Proximas Citas",
    "11. Salir",
)

def print_menu() -> str:
    valid_options = {str(number) for number in range(1, len(OPTIONS) + 1)}

    while True:
        print("=== Menú de Opciones ===")
        for option in OPTIONS:
            print(option)

        option = input("Ingrese Opción Deseada: ").strip()
        if option in valid_options:
            return option

        print(
            "Opción Seleccionada Invalida. Intente de Nuevo o digite 11 para salir"
            )

def print_table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> None:
    if not rows:
        print("Sin datos")
        return

    widths = [
        max(
            len(str(headers[index])),
            *(len(str(row[index])) for row in rows),
        )
        for index in range(len(headers))
    ]

    row_format = "  ".join(f"{{:<{width}}}" for width in widths)
    print(row_format.format(*headers))
    print("  ".join("-" * width for width in widths))

    for row in rows:
        print(row_format.format(*row))