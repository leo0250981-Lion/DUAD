#Class "Person"
class Person:
    def __init__(self, name):
        self.name = name

#Class "Bus"
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} stepped on the bus")
        else:
            print("The bus is full")

    def remove_passenger(self):
        if self.passengers:
            passenger = self.passengers.pop()
            print(f"{passenger.name} stepped out of the bus")
        else:
            print(" There are no passengers in the bus, bus is currently empty")

#Example
bus = Bus(2)

p1 = Person("Carlos")
p2 = Person("Ana")
p3 = Person("Luis")

bus.add_passenger(p1)
bus.add_passenger(p2)
bus.add_passenger(p3)  # Bus is Full

bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()  #Empty Bus