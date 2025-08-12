import json
from locust import task, SequentialTaskSet
import random


class DataTasks(SequentialTaskSet):
    def on_start(self):
        self.created_item_id = None
        self.step = 0

    @task
    def run_sequence(self):
        if self.step == 0:
            self.get_items()
            self.step += 1
        elif self.step == 1:
            self.add_item()
            self.step += 1
        elif self.step == 2:
            self.update_item()
            self.step += 1
        elif self.step == 3:
            self.delete_item()
            self.step += 1
        else:
            self.interrupt()

    def get_items(self):
        self.client.get("/items", name="Getting all the items")

    def add_item(self):
        new_item = {
            "name": f"Item {random.randint(1, 1000)}",
            "price": round(random.uniform(10.0, 500.00), 2),
            "stock": random.randint(1, 100)
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post("/items", data=json.dumps(new_item),
                                    headers=headers, name="Adding Item")

        if response.status_code == 201:
            item_id = response.json().get("id")
            self.created_item_id = item_id
            print(f"Created new item {item_id}")
        else:
            print(f"Error creating item {response.text}")

    def update_item(self):
        item_id = self.created_item_id
        new_item = {
            "stock": random.randint(1, 100)
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.put(f"/items/{item_id}",
                                   data=json.dumps(new_item),
                                   headers=headers, name="Update item")

        if response.status_code == 200:
            item_id = response.json().get("id")
            self.created_item_id = item_id
            print(f"Update item {item_id}")
        else:
            print(f"Error accessing item {response.text}")

    def delete_item(self):
        item_id = self.created_item_id
        self.client.delete(f"/items/{item_id}", name="Delete Item")
        print(f"Delete item: {item_id}")
        self.created_item_id = None
