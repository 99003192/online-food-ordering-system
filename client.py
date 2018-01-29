from requests import put, get, post

restaurants = {
    '1': {'name': 'Panda', 'address': '15 street'},
    '2': {'name': 'Mr Chen', 'address': 'Hackbeery'},
    '3': {'name': 'Swen', 'address': 'Univ. Blvd'},
}

menus = {
    '1': {'restaurant': '1', 'type': 'breakfast'},
    '2': {'restaurant': '1', 'type': 'lunch'},
    '3': {'restaurant': '2', 'type': 'dinner'},
}

for id in restaurants:
    info = restaurants[id]
    post('http://localhost:5000/restaurant/' + id, data={'name': info['name'], 'address': info['address']})

for id in restaurants:
    r = get('http://localhost:5000/restaurant/' + id)
    print(r.json())
