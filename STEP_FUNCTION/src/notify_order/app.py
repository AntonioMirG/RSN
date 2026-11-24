def lambda_handler(event, context):
    """Simula una notificación de éxito o de error."""
    notification_type = event.get("notificationType", "UNKNOWN")
    order = event.get("order", {})
    order_id = order.get("orderId") or order.get("validation", {}).get("orderId")

    return {
        "sent": True,
        "type": notification_type,
        "orderId": order_id,
        "message": (
            "Notificación de éxito enviada"
            if notification_type == "SUCCESS"
            else "Notificación de error enviada"
        ),
    }
