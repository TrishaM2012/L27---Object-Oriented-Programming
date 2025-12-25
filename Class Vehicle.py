class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
model1X = vehicle(240,18)

print("Model Max Speed:", model1X.max_speed)
print("Model Mileage:", model1X.mileage)
        