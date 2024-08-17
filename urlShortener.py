import requests

API_KEY = 'e35e2ca312c0cb2a119e2c2c263dd0940ff4ede6'
BASE_URL = 'https://api-ssl.bitly.com/v4/shorten'

def shorten_link(full_link: str):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    payload = {
        'long_url': full_link
    }

    # Print debug information
    # print("Headers:", headers)
    # print("Payload:", json.dumps(payload, indent=4))

    response = requests.post(BASE_URL, json=payload, headers=headers)
    # print(f'Status Code: {response.status_code}')
    # print(f'Response Text: {response.text}')

    if response.status_code in [200, 201]:
        return response.json().get('link')
    else:
        if response.status_code == 403:
            print("Check your API key and permissions.")
        return f"Error: {response.status_code}, {response.text}"

def main():
    input_link: str = input('Enter a link: ')
    shortened_link = shorten_link(input_link)
    print(f'The shortened link: {shortened_link}')

if __name__ == '__main__':
    main()



# Here's a step-by-step breakdown of how I knew to make these changes:
#
# Authorization Header:
#
# Most APIs that require an API key for authentication expect it to be included in the headers. This is a common practice for RESTful APIs to ensure that the key is not exposed in the URL or payload.
# The Authorization header with the Bearer token format is a standard method for passing the API key securely.
# Content-Type Header:
#
# When sending JSON data in the body of a POST request, it is standard to set the Content-Type header to application/json to inform the server of the data format.
# Payload:
#
# From experience with similar APIs, I know that the payload usually contains the primary data the API needs to perform its function. In this case, Bitly needs the long_url to shorten it.
# The key field you initially had is not required in the payload since the API key is provided in the headers.
# Requests:
#
# The requests.post method is used to send a POST request. This is necessary for submitting data to the API endpoint to create a new resource (a shortened URL in this case).
# Response Handling:
#
# Checking the status code of the response is a common practice to handle errors gracefully. A status code of 200 typically indicates success.
# Parsing the JSON response to extract the relevant data (the shortened URL) is a standard way to handle API responses that return data in JSON format.
# Tips for Using API Documentation
# When using API documentation, look for the following key sections:
#
# Authentication: Details on how to include your API key or other credentials.
# Endpoints: Information on the different URLs you can send requests to.
# Request Headers: Any headers that need to be included in your requests.
# Request Body: The format and required fields for the data you need to send.
# Response: Examples of successful and error responses, including status codes and response body structure.
# These sections will give you the necessary information to correctly format your requests and handle responses.