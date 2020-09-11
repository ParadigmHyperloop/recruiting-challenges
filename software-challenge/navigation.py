"""
You will be implementing a hypothetical navigation class,
which keeps track of the boring machine's current position, its desired position,
and makes any adjustments necessary to keep the machine on track.You will make the
assumption that two other interfaces are written to make your life easier, the GPS
class will interface with our onboard GPS sensor to get thecurrent position, and
the Steering class will control the actuation necessary to move the borer left or
right (using left, right, and distance to as opposed to actual coordinates
for simplicity)
"""

""" VISUALIZATION OF COORDINATE PLANE FOR STEERING

x-Plane
    behind target --------------- target

y-Plane
    left of target ---------------target------------------ right of target

z-Plane
    above target
    |
    |
    |
    |
    |
    target
    |
    |
    |
    |
    |
    below target
"""

""" Class to control position based on GPS input """
class Navigation:
    def __init__(self, GPS, steering):
        self.GPS = GPS
        self.steering = steering

        # These will be tuples of the form (x, y, z)
        self.current_position = None
        self.desired_position = None
    
    """ Sets the desired position that the borer will attempt to move to
    
    Note: assume the user will pass in the desired_position parameter when using
          the interface
    """
    def set_desired_position(self, desired_position):
        pass

    """ Updates the current position """
    def update_current_position(self):
        pass

    """ Navigate to the desired position from the current position
    
    Based on the current position tuple, compared to the desired position tuple,
    make decisions on steering, and ensure that the actuations are successful

    Returns: True if actuation requests were successful, False if not
    Note: It may be good to notify the user if something unexpected happens!
    """
    def navigate(self):
        pass


# Code below is provided for you, DO NOT NEED TO IMPLEMENT

""" Interfaces with the GPS Sensor """
class GPS:
    def __init__(self, GPSSensor):
        self.GPS = GPSSensor
        self.x = GPSSensor.pos.x
        self.y = GPSSensor.pos.y
        self.z = GPSSensor.pos.z

    """ Polls the GPS for the current position

    Modifies the leftOf, rightOf, and tunnelPos fields to contain the current
    position
    """
    def pollSensor(self):
        self.x, self.y, self.z = self.GPS.updatePosition()
    
    """ Returns the positions stored in the leftOf, rightOf, and tunnelPos fields as a tuple """
    def getPos(self):
        return self.x, self.y, self.z

""" Interfaces with the actuator which steers the tunnel borer, and controls its speed """
class Steering:
    def __init__(self, actuation_component):
        self.act = actuation_component

    """ Steers the borer to the left

    Returns: True if the actuation is successful, False if it is not
    """
    def move_left(self, left_distance):
        return self.act.steer_left(left_distance)
        
    """ Steers the borer to the right

    Returns: True if the actuation is successful, False if it is not
    """
    def move_right(self, right_distance):
        return self.act.steer_right(right_distance)

    """ Steers the borer down

    Returns: True if the actuation is successful, False if it is not
    """
    def move_down(self, down_distance):
        return self.act.steer_down(down_distance)

    """ Steers the borer to the right

    Returns: True if the actuation is successful, False if it is not
    """
    def move_up(self, up_distance):
        return self.act.steer_up(up_distance)

    """ Moves the borer forward

    Returns: True if the motor sucessfully moves the borer, False if it is not
    """
    def move_forward(self):
        return self.act.forward()

    """ Stops the borer from moving

    Returns: True if the motor stops the borer, False if it does not
    """
    def stop(self):
        return self.act.stop()
