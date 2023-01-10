import math
import turtle
import itertools


class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0),
        velocity=(0, 0)
    ) -> None:
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity

        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size
        )

        self.penup()
        self.hideturtle()

        solar_system.add_body(self)
    
    def draw(self) -> None:
        self.clear()
        self.dot(self.display_size)
    
    def move(self) -> None:
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class SolarSystem():
    def __init__(self, width: int, height: int) -> None:
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(
            width=width, height=height
        )
        self.solar_system.bgcolor('black')

        self.bodies = []

    def add_body(self, body: SolarSystemBody) -> None:
        self.bodies.append(body)

    def remove_body(self, body: SolarSystemBody) -> None:
        body.clear()
        self.bodies.append(body)
    
    def update_all(self) -> None:
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()
    
    @staticmethod
    def acceleration_due_to_gravity(
        first: SolarSystemBody,
        second: SolarSystemBody
    ) -> None:
        force = first.mass * second.mass / (first.distance(second) ** 2)
        angle = first.towards(second)
        reverse = 1
        
        for body in first, second:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y)
            )
            reverse = -1
    
    def check_collision(
        self,
        first: SolarSystemBody,
        second: SolarSystemBody
    ) -> None:

        if isinstance(first, Planet) and isinstance(second, Planet):
            return

        if first.distance(second) < first.display_size / 2 + second.display_size / 2:
            for body in first, second:
                if isinstance(body, Planet):
                    self.remove_body(body)
    
    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx+1:]:
                self.acceleration_due_to_gravity(first, second)
                self.check_collision(first, second)


class Sun(SolarSystemBody):
    def __init__(
        self, 
        solar_system, 
        mass, 
        position=(0, 0), 
        velocity=(0, 0)
    ) -> None:

        super().__init__(
            solar_system, 
            mass, 
            position, 
            velocity
        )
        self.color('yellow')


class Planet(SolarSystemBody):
    colors = itertools.cycle(["red", "green", "blue", "brown"])

    def __init__(
        self, 
        solar_system, 
        mass, 
        position=(0, 0), 
        velocity=(0, 0)
    ) -> None:
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colors))
    
