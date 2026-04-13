def limpiar_dinero(valor):
    """
    Convierte strings de moneda (ej: €110.5M) a valores numéricos flotantes.
    Elimina el símbolo de Euro y multiplica según sufijos K (miles) o M (millones).
    """
    if valor is None:
        return 0.0

    if isinstance(valor, str):
        valor = valor.replace('€', '').strip()

        try:
            if 'M' in valor:
                return float(valor.replace('M', '')) * 1_000_000
            elif 'K' in valor:
                return float(valor.replace('K', '')) * 1_000
            else:
                return float(valor)
        except ValueError:
            return 0.0

    return float(valor)


def limpiar_altura(valor):
    """
    Normaliza la altura a centímetros.
    Maneja tanto el formato métrico (180cm) como el imperial (5'11").
    """
    if valor is None:
        return 0.0

    valor = str(valor).strip()

    try:
        if "'" in valor:  # Formato pies'pulgadas
            pies, pulgadas = valor.split("'")
            pulgadas = pulgadas.replace('"', '')
            return round((int(pies) * 30.48) + (int(pulgadas) * 2.54), 1)

        return float(valor.replace('cm', ''))

    except ValueError:
        return 0.0


def limpiar_peso(valor):
    """
    Normaliza el peso a kilogramos.
    Maneja tanto kg como lbs (libras).
    """
    if valor is None:
        return 0.0

    valor = str(valor).strip()

    try:
        if 'lbs' in valor:
            return round(float(valor.replace('lbs', '')) * 0.453592, 1)

        return float(valor.replace('kg', ''))

    except ValueError:
        return 0.0
