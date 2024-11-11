import requests
import boto3
import uuid

def lambda_handler(event, context):
    # URL de la API de IGP para obtener los últimos sismos
    url = "https://ultimosismo.igp.gob.pe/api/ultimo-sismo/ajaxb/2024"

    # Realizar la solicitud HTTP a la API
    response = requests.get(url)
    if response.status_code != 200:
        return {
            'statusCode': response.status_code,
            'body': 'Error al acceder a la API de sismos'
        }

    # Obtener los datos de la respuesta JSON
    sismos = response.json()

    # Verificar si hay datos en la respuesta
    if not sismos:
        return {
            'statusCode': 404,
            'body': 'No se encontraron sismos en la respuesta de la API'
        }

    # Tomar los últimos 10 sismos
    ultimos_sismos = sismos[:10]

    print(ultimos_sismos)
    '''
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaSismos')

    # Eliminar todos los elementos de la tabla antes de agregar los nuevos
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'id': each['id']
                }
            )

    # Insertar los datos de los últimos 10 sismos en DynamoDB
    for sismo in ultimos_sismos:
        sismo['id'] = str(uuid.uuid4())  # Generar un ID único para cada entrada
        table.put_item(Item=sismo)

    # Retornar el resultado como JSON
    return {
        'statusCode': 200,
        'body': ultimos_sismos
    }
    '''

lambda_handler(None, None)