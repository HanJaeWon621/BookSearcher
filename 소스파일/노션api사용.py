import requests

# Set the URL and headers
url = "https://api.notion.com/v1/search"
headers = {
    "Authorization": "secret_8rp93gMC8IweVNqVmZO3vpYlo0gPnm9RkMPePfHx3kK",
    "Notion-Version": "2022-02-22"
}

# Set the query and filter parameters
params = {
    "query": "",
    "filter": {
        "property": "object",
        "value": "page"
    }
}

# Send the request and get the response
response = requests.get(url, headers=headers, params=params)
pages = response.json()["results"]

# Print the page titles
for page in pages:
    print(page["title"][0]["text"]["content"])
