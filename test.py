import requests

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer oYLcGN99G6qjE8-V-l9oCDsgQeZUNIibMCf6abFPZQ25cKhYnJTd9dGWo9MHFmXUCZSe6BT1FDIk3c3aAy62hBPQ6kmp6fHrEuaWzDMeVMurmVXhH1C-z7Wt9SY9ZnYx"
}
params = {
    "location": "Zürich",
    "limit": 10,
    "categories": "italian",
    "price": "3"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())