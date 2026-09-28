from datetime import datetime
from typing import Callable, Sequence

from dentistryapp.parameters import Parameters


CANCEL_KEYWORDS = {"cancelar", "c"}


def _read_until_valid(
    prompt: str,
    validator: Callable[[str], bool],
    error_message: str,
) -> str | None:
    value = input(f"{prompt}: ").strip()

    while value.lower() not in CANCEL_KEYWORDS and not validator(value):
        value = input(
            f"{error_message}. Ingrese un valor válido o escriba "
            "'Cancelar' para volver al menú principal: "
        ).strip()

    return None if value.lower() in CANCEL_KEYWORDS else value


def read_valid_ID(prompt: str = "Documento de Identidad") -> int | None:
    value = _read_until_valid(
        prompt,
        str.isdigit,
        "Documento de Identidad Invalido",
    )
    return int(value) if value is not None else None


def read_valid_name(prompt: str = "Nombre del Paciente") -> str | None:
    return _read_until_valid(
        prompt,
        lambda value: value.replace(" ", "").isalpha(),
        "Nombre Invalido",
    )


def read_valid_phone(prompt: str = "Numero de Telefono") -> str | None:
    return _read_until_valid(
        prompt,
        str.isdigit,
        "Teléfono inválido, debe contener solo números",
    )


def read_valid_choice(
    prompt: str,
    valid_options: Sequence[str],
) -> str | None:
    options_text = ", ".join(valid_options)
    options_by_lower = {option.lower(): option for option in valid_options}

    value = _read_until_valid(
        f"{prompt} ({options_text})",
        lambda candidate: candidate.lower() in options_by_lower,
        f"Valor inválido, las opciones válidas son: {options_text}",
    )
    return options_by_lower[value.lower()] if value is not None else None


def read_valid_quantity( 
        attention_type: str,
        prompt: str = "Ingrese la cantidad",) -> int | None:
    if attention_type in Parameters.SINGLE_QUANTITY_ATTENTION_TYPES:
        error_message = (
            f"Cantidad inválida, para {attention_type} la cantidad debe ser 1"
            )
    else:
        error_message = "Cantidad inválida, debe ser un número entero mayor que cero"

    value = _read_until_valid(
        prompt,
        lambda candidate: candidate.isdigit()
        and int(candidate) > 0
        and (
            attention_type not in Parameters.SINGLE_QUANTITY_ATTENTION_TYPES
            or int(candidate) == 1
        ),
        error_message,
    )
    return int(value) if value is not None else None


def read_valid_date(
    prompt: str = "Fecha y hora de la cita (Formato AAAA-MM-DD HH:MM)",
) -> str | None:
    def is_valid_date(value: str) -> bool:
        try:
            parsed = datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError:
            return False
        return parsed >= datetime.now()

    return _read_until_valid(
        prompt,
        is_valid_date,
        "Verifique la Fecha Ingresada y el formato AAAA-MM-DD HH:MM "
        f"(Ejemplo: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    )
