""" navigation.py

You will be implementing a hypothetical navigation class,
which keeps track of the TBM's current position, its desired position,
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
    
Misc:
    TBM - Tunnel Boring Machine
"""

# Implement this class - this code will not actually be run, it is more of a thought exercise!
class Navigation:
    """ Class to control position based on GPS input 
    
    Attributes:
        GPS - GPS Interface object, used to obtain GPS coordinates
        steering - Steering object
        current_position - The current position of the TBM in 3-D space (x, y, z)
        desired_position - The desired position of the TBM in 3-D space (x, y, z)
    
    Methods:
        set_desired_position() 
        update_current_position()  
        navigate()
    """
    
    def __init__(self, GPS, steering):

        # Instances of the two classes defined below for use to complete the navigation method
        self.GPS = GPS
        self.steering = steering

        # These will be tuples of the form (x, y, z)
        self.current_position = None
        self.desired_position = None
    

    def set_desired_position(self, desired_position):
        """ Sets the desired position the TBM will attempt to move to.
        
        Note: assume the user will pass in the desired_position parameter when using
        the interface 
        """
        # This sets the desired position to the value passed by the user when they use the UI
        self.desired_position = desired_position


    def update_current_position(self):
        """ Updates the current position of the TBM """
        # This updates the current position
        self.current_position = self.GPS.getPos()


    def navigate(self):
        """ Navigate to the desired position from the current position
        
        Based on the current position tuple, compared to the desired position tuple,
        make decisions on steering, and ensure that the actuations are successful
        Returns: True if actuation requests were successful, False if not
        Note: It may be good to notify the user if something unexpected happens!

        This method was implemented by identifying the difference in the desired position
        and the current position. Each difference was stored in the variables x, y, and z.
        Based on these variables, actuations are attempted to move TBM.
        If all actuations were successful, this method returns True, and the user is notified
        that everything went well! Otherwise, the user is notified that actuations were 
        unsuccesful in the corresponding direction (x, y, or z). 
        """
        # Evaluate the differences of each position for x, y, and z
        x = self.desired_position[0] - self.current_position[0]
        y = self.desired_position[1] - self.current_position[1]
        z = self.desired_position[2] - self.current_position[2]

        # First check the x component and attempt actuation
        if (x > 0):
            x_act = self.steering.move_forward(x)
        else:
            x_act = self.steering.stop()

        # Next check the y component and attempt actuation
        if (y > 0):
            y_act = self.steering.move_right(y)
        elif (y < 0):
            y_act = self.steering.move_left(y)
        else:
            y_act = self.steering.stop()

        # Lastly, check the z component and attempt actuation
        if (z > 0):
            z_act = self.steering.move_up(z)
        elif (z < 0):
            z_act = self.steering.move_down(z)
        else:
            z_act = self.steering.stop()

        # Check if all actuations were successful! Return True if all were successful.
        if x_act and y_act and z_act:
            print("All actuations were successful :D")
            return True

        # Next check all the actuations and print out to the user where TBM is running into errors for either x, y, or z.
        if not x_act:
            print("Something went wrong with the actuation moving in the x-direction!")
        if not y_act:
            print("Something went wrong with the actuation moving in the y-direction!")
        if not z_act:
            print("Something went wrong with the actuation moving in the z-direction!")

        # If not all of the actuations were successful, return False
        return False


# Code below is provided for you, YOU DO NOT NEED TO IMPLEMENT THIS
   
class GPS:
    """ Mock GPS sensor interface class """
    
    def __init__(self, GPSSensor):
        self.GPS = GPSSensor
        self.x = GPSSensor.pos.x
        self.y = GPSSensor.pos.y
        self.z = GPSSensor.pos.z

    def pollSensor(self):
        """ Polls the GPS for the current position

        Updates the current position by reading the gps sensor
        """
        self.x, self.y, self.z = self.GPS.read()
    
    def getPos(self):
        """ Returns the TBM position """
        return self.x, self.y, self.z

class Steering:
    """ Interfaces with the actuator which steers the TBM, and controls its speed 
    
    Attributes:
        act - Placeholder actuation component (could be a motor for example, or some other actuator related to steering)

    Methods:
        move_left(left_distance)
        move_right(right_distance)
        move_down(down_distance)
        move_up(up_distance)
        move_forward()
        stop()
    """
    
    def __init__(self, actuation_component):
        self.act = actuation_component

    def move_left(self, left_distance):
        """ Steers the TBM left

        Returns: True if the actuation is successful, False if it is not
        """
        return self.act.steer_left(left_distance)
        
    def move_right(self, right_distance):
        """ Steers the TBM to the right

        Returns: True if the actuation is successful, False if it is not
        """
        return self.act.steer_right(right_distance)

    def move_down(self, down_distance): 
        """ Steers the TBM down

        Returns: True if the actuation is successful, False if it is not
        """
        return self.act.steer_down(down_distance)

    def move_up(self, up_distance):
        """ Steers the TBM to the right

        Returns: True if the actuation is successful, False if it is not
        """
        return self.act.steer_up(up_distance)

    def move_forward(self):
        """ Moves the TBM forward

        Returns: True if the motor sucessfully moves the TBM, False if it is not
        """
        return self.act.forward()

    def stop(self):
        """ Stops the TBM from moving

        Returns: True if the motor stops the TBM, False if it does not
        """
        return self.act.stop()