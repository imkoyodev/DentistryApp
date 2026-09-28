class Parameters:
    """
    Parametros y aliases permitidos por la aplicación
    """

    PARTICULAR = "Particular"
    EPS = "EPS"
    PREPAGADA = "Prepagada"

    LIMPIEZA = "Limpieza"
    CALZA = "Calza"
    EXTRACCION = "Extracción"
    DIAGNOSTICO = "Diagnóstico"

    REGULAR = "Regular"
    PRIORITARIO = "Prioritario"

    CLIENT_TYPES = (PARTICULAR, EPS, PREPAGADA)
    ATTENTION_TYPES = (LIMPIEZA, CALZA, EXTRACCION, DIAGNOSTICO)
    ATTENTION_PRIORITY = (REGULAR, PRIORITARIO)

    SINGLE_QUANTITY_ATTENTION_TYPES = (LIMPIEZA, DIAGNOSTICO)