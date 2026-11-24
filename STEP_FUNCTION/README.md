# Demo AWS Step Functions + Lambda

Demo pequeña para AWS Learner Lab que muestra:

- `Choice`: separa pedidos válidos e inválidos.
- `Retry`: reintenta errores transitorios de las tareas Lambda.
- `Catch`: captura errores y dirige el flujo a una notificación de error.
- Tres funciones Lambda escritas en Python 3.12.

## 1. Validar y desplegar

```bash
sam validate
sam build
sam deploy \
  --stack-name step-functions-lambda-demo \
  --resolve-s3 \
  --capabilities CAPABILITY_IAM \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset
```

El despliegue crea las Lambdas y la Step Function. Usa el rol preexistente
`LabRole`, disponible normalmente en AWS Learner Lab, para evitar permisos
adicionales de IAM. El ARN de la Step Function se muestra al final como
`StateMachineArn`.

## 2. Ejecutar ejemplos

Guarda el ARN mostrado por CloudFormation en una variable:

```bash
STATE_MACHINE_ARN="arn:aws:states:REGION:ACCOUNT_ID:stateMachine:step-functions-lambda-demo"
```

Pedido válido (camino de éxito):

```bash
aws stepfunctions start-execution \
  --state-machine-arn "$STATE_MACHINE_ARN" \
  --input file://events/valid.json
```

Pedido inválido (camino `Choice` -> `PedidoInvalido`):

```bash
aws stepfunctions start-execution \
  --state-machine-arn "$STATE_MACHINE_ARN" \
  --input file://events/invalid.json
```

Error simulado (observa tres intentos y después `Catch`):

```bash
aws stepfunctions start-execution \
  --state-machine-arn "$STATE_MACHINE_ARN" \
  --input file://events/error.json
```

Para consultar una ejecución:

```bash
aws stepfunctions describe-execution --execution-arn "EXECUTION_ARN"
```

## 3. Eliminar recursos

```bash
sam delete --stack-name step-functions-lambda-demo
```

El archivo `events/error.json` activa intencionadamente una excepción en
`ProcessOrderFunction`. No uses datos reales: es únicamente una demostración.
