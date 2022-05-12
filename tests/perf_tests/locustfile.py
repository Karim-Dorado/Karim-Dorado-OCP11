from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    
    def on_start(self):
        self.client.post("showSummary", {"email": "john@simplylift.co"})

    def on_stop(self):
        self.client.get("logout")

    @task
    def board(self):
        self.client.get("")

    @task
    def booking(self):
        name = "Simply Lift"
        competition = "Fall Classic"
        self.client.get(f"book/{competition}/{name}")

    @task
    def purchase(self):
        self.client.post("purchasePlaces", data={
            "club": "Simply Lift",
            "competition": "Fall Classic",
            "places": 5
        })
