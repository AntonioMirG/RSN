def lambda_handler(event, context):
    """Valida un pedido y devuelve el resultado para el estado Choice."""
    required_fields = ("orderId", "customer", "amount")
    missing_fields = [field for field in required_fields if field not in event]
    amount = event.get("amount")

    valid = not missing_fields and isinstance(amount, (int, float)) and amount > 0
    return {
        "valid": valid,
        "orderId": event.get("orderId"),
        "reason": (
            "OK"
            if valid
            else f"Datos inválidos: faltan {', '.join(missing_fields)}"
            if missing_fields
            else "amount debe ser un número mayor que cero"
        ),
    }
