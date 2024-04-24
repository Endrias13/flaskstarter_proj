from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Simulate real user waiting time between requests (1 to 5 seconds).

    @task
    def load_prediction(self):
        # This is the data payload for the prediction. Adjust the keys and values based on your model's input requirements.
        payload = {
            "CHAS": {"0": 0},
            "RM": {"0": 6.575},
            "TAX": {"0": 296.0},
            "PTRATIO": {"0": 15.3},
            "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}
        }
        
        headers = {'content-type': 'application/json'}
        
        # Send a POST request to the prediction endpoint
        self.client.post("/predict", json=payload, headers=headers)