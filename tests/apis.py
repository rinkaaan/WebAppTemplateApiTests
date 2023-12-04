import os

import openapi_client
from dotenv import load_dotenv

load_dotenv()
configuration = openapi_client.Configuration(
    host="http://localhost:8080",
)
configuration.access_token = os.getenv("API_ACCESS_TOKEN")

api = openapi_client.ApiClient(configuration)
petApi = openapi_client.PetApi(api)
