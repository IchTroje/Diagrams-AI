from rest_framework.test import APITestCase
from rest_framework import status
import json


class SendPromptTest(APITestCase):
    def test_send_prompt(self):
        url = "/send_prompt/"
        data = {"body": "Twój prompt"}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        response_data = response.json()

        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], "Twój prompt")

    def test_send_long_prompt(self):
        url = "/send_prompt/"
        data = {"body": "A" * 1000}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], "A" * 1000)

    def test_invalid_json(self):
        url = "/send_prompt/"
        invalid_data = "{ body: 'This is wrong JSON' }"

        response = self.client.post(url, invalid_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data["message"], "Niepoprawny format JSON")

    def test_empty_prompt(self):
        url = "/send_prompt/"
        data = {"body": ""}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data["message"], "Proszę wprowadzić treść promptu.")

    def test_send_large_prompt(self):
        url = "/send_prompt/"
        data = {"body": "B" * 10000}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], "B" * 10000)

    def test_invalid_json_format(self):
        url = "/send_prompt/"
        invalid_data = '{body: "This is invalid"}'

        response = self.client.post(url, invalid_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data["message"], "Niepoprawny format JSON")

    def test_send_prompt_success(self):
        url = "/send_prompt/"
        data = {"body": "Valid prompt"}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertEqual(response_data["message"], "Valid prompt")

    def test_send_prompt_failure(self):
        url = "/send_prompt/"
        data = {}

        response = self.client.post(
            url, json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        response_data = response.json()
        self.assertEqual(response_data["message"], "Proszę wprowadzić treść promptu.")
