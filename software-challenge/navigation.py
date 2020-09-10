"""
You will be implementing a hypothetical navigation sensor class,
which keeps track of the boring machine's current position, its desired position,
and makes any adjustments necessary to keep the machine on track.You will make the
assumption that two other interfaces are written to make your life easier, the GPS
class will interface with our onboard GPS sensor to get thecurrent position, and
the Steering class will control the actuation necessary to move the borer left or
right (using left, right, and distance to as opposed to actual coordinates
for simplicity)
"""

"""Class to control position based on GPS input
"""
class Navigation:
    def __init__(self, GPS, steering):
        self.GPS = GPS
        self.steering = steering
        self.position = None
    def update_position(self, GPS):
        pass

# Code below is provided for you, DO NOT NEED TO IMPLEMENT

""" Interfaces with the GPS Sensor """
class GPS:
    def __init__(self, GPSSensor):
        self.GPS = GPSSensor
        self.leftOf = GPSSensor.pos.left
        self.rightOf = GPSSensor.pos.right
        self.tunnelPos = GPSSensor.pos.track

    """ Polls the GPS for the current position

    Modifies the leftOf, rightOf, and tunnelPos fields to contain the current
    position
    """
    def pollSensor(self):
        self.leftOf, self.rightOf, self.tunnelPos = self.GPS.updatePosition()
    
    """ Returns the positions stored in the leftOf, rightOf, and tunnelPos fields as a tuple """
    def getPos(self):
        return self.leftOf, self.rightOf, self.tunnelPos

""" Interfaces with the actuator which steers the tunnel borer """
class Steering:

    """
    """
    def __init__(self, actuation_component):
        self.act = actuation_component

    """ Steers the borer to the left

    Returns: True if the actuation is successful, False if it is not
    """
    def move_left(self, left_distance):
        return self.act.steer_left(left_distance)