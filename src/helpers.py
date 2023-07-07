import openai
import os
import boto3
from requests_aws4auth import AWS4Auth
from time import sleep

openai.api_key = os.environ.get('OPENAI_API_KEY')

def get_embeddings_with_retry(text):
    ctr = 0
    while (ctr < 4):
        ctr += 1
        try:
            embedding = openai.Embedding.create(
                input=text,
                model="text-embedding-ada-002"
            )['data'][0]['embedding']
            return embedding
        except:
            sleep(1)
    print("Unsuccessful at getting embeddings for:", text)

def get_aws_auth(region):
    session = boto3.Session(profile_name='default') # this profile has to match the iam user who's the master user for your OpenSearch cluster
    creds = session.get_credentials()
    auth = AWS4Auth(creds.access_key, creds.secret_key, region, 'es')
    return auth