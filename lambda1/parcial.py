import json
import boto3
import requests
from datetime import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'parci4l3'

def lambda_handler(event, context):
    now = datetime.utcnow().strftime('%Y-%m-%d')
    urls = {
        'eltiempo': 'https://www.eltiempo.com',
        'publimetro': 'https://www.publimetro.co/'
    }

    for name, url in urls.items():
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content = response.text

            key = f"headlines/raw/{name}-contenido-{now}.html"
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=key,
                Body=content,
                ContentType='text/html'
            )
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            continue

    return {
        'statusCode': 200,
        'body': json.dumps('Scraping completado exitosamente')
    }