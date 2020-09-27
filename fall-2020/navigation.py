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

        self.desired_position = desired_position

        pass

    
    def update_current_position(self):
        """ Updates the current position of the TBM """
        GPS.pollSensor
        self.current_position = GPS.getPos
        
        pass


    def navigate(self):
        """ Navigate to the desired position from the current position
        
        Based on the current position tuple, compared to the desired position tuple,
        make decisions on steering, and ensure that the actuations are successful

        Returns: True if actuation requests were successful, False if not
        Note: It may be good to notify the user if something unexpected happens!
        """
        act_request_forward = True
        act_request_right = True
        act_request_left = True
        act_request_up = True
        act_request_down = True

        if desired_position[0] > current_position[0]:
            while(current_position[0] != desired_position[0]):
                act_request_forward = Steering.move_forward()
                self.update_current_position
                if act_request_forward == False:
                    print("Unable to move to desired x position")
        
        required_y_distance = desired_position[1] - current_position[1]
        if required_y_distance > 0:
            act_request_right = Steering.move_right(required_y_distance)
        elif required_y_distance < 0:
            act_request_left = Steering.move_left(required_y_distance)
        if act_request_left or act_request_left == False:
            print("Unable to move to desired y position")
            
        required_z_distance = desired_position[2] - current_position[2]
        if required_z_distance > 0:
            act_request_up = Steering.move_up(required_z_distance)
        elif required_z_distance < 0:
            act_request_down = Steering.move_down(required_z_distance)        
        if act_request_up or act_request_down == False:
            print("Unable to move to desired z position")       

        self.update_current_position
        return current_position == desired_position
        
        pass


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
    
