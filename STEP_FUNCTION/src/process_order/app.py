def lambda_handler(event, context):
    """Procesa el pedido; simulateError permite observar Retry y Catch."""
    if event.get("simulateError") is True:
        raise RuntimeError("Error simulado durante el procesamiento")

    return {
        "status": "COMPLETED",
        "orderId": event["orderId"],
        "message": "Pedido procesado correctamente",
    }
