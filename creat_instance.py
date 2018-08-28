def create_servers(self):
        url = "http://192.168.20.20:8774/v2.1/flavors"
        data = {
            "flavor": {
                "name": "test_flavor_2",
                "ram": 256,
                "vcpus": 1,
                "disk": 10,
                "id": "10",
                "rxtx_factor": 2.0
            }
        }
        response = self._post_request(url, data)
        print json.dumps(response,indent=4)
        return response
