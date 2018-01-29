import unittest
import json

from requests import put, get, post, delete

restaurants = {
    1: {'name': 'Panda', 'address': '15 street'},
    2: {'name': 'Mr Chen', 'address': 'Hackbeery'},
    3: {'name': 'Swen', 'address': 'Univ. Blvd'},
}

menus = {
    1: {'restaurant': '1', 'type': 'breakfast'},
    2: {'restaurant': '1', 'type': 'lunch'},
    3: {'restaurant': '2', 'type': 'dinner'},
}

items = {
    1: {'menu': '1', 'name': 'egg'},
    2: {'menu': '2', 'name': 'chicken'},
    3: {'menu': '3', 'name': 'sushi'},
}


class RestApiTest(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://localhost:5000'

    def test_restaurant_api(self):
        for restaurant_id in restaurants:
            info = restaurants[restaurant_id]
            # add a new entry
            r = post(self.Url + '/restaurant/' + str(restaurant_id),
                     data={'name': info['name'], 'address': info['address']})
            self.assertEqual(r.status_code, 200)
            # get an entry
            r = get(self.Url + '/restaurant/' + str(restaurant_id))
            self.assertEqual(r.json(), json.dumps({'id': restaurant_id, 'info': info}))
            # update an entry
            r = put(self.Url + '/restaurant/' + str(restaurant_id),
                    data={'name': info['name'], 'address': info['address']})
            self.assertEqual(r.status_code, 200)
            # delete an entry
            r = delete(self.Url + '/restaurant/' + str(restaurant_id))
            self.assertEqual(r.status_code, 204)

    def test_menu_api(self):
        for menu_id in menus:
            info = menus[menu_id]
            # add a new entry
            r = post(self.Url + '/menu/' + str(menu_id),
                     data={'restaurant': info['restaurant'], 'type': info['type']})
            self.assertEqual(r.status_code, 200)
            # get an entry
            r = get(self.Url + '/menu/' + str(menu_id))
            self.assertEqual(r.json(), json.dumps({'id': menu_id, 'info': info}))
            # update an entry
            r = put(self.Url + '/menu/' + str(menu_id),
                    data={'restaurant': info['restaurant'], 'type': info['type']})
            self.assertEqual(r.status_code, 200)
            # delete an entry
            r = delete(self.Url + '/menu/' + str(menu_id))
            self.assertEqual(r.status_code, 204)

    def test_item_api(self):
        for item_id in items:
            info = items[item_id]
            # add a new entry
            r = post(self.Url + '/item/' + str(item_id), data={'menu': info['menu'], 'name': info['name']})
            self.assertEqual(r.status_code, 200)
            # get an entry
            r = get(self.Url + '/item/' + str(item_id))
            self.assertEqual(r.json(), json.dumps({'id': item_id, 'info': info}))
            # update an entry
            r = put(self.Url + '/item/' + str(item_id),
                    data={'menu': info['menu'], 'name': info['name']})
            self.assertEqual(r.status_code, 200)
            # delete an entry
            r = delete(self.Url + '/item/' + str(item_id))
            self.assertEqual(r.status_code, 204)


if __name__ == '__main__':
    unittest.main()
