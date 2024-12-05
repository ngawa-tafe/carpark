class Display:
    def __init__(self, id, car_park, message=" ", is_on="false"):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update(self, data):
        for key, value in data.items():
            if key == "message":
                self.message = value
            else:
                print(f"{key}: {value}")

    def __str__(self):
        return f"Display {self.id}: {self.message}."
