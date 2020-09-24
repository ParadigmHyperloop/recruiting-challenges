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
        #added a boolean to check whether the navigate is using a new desired position or a previously added one which has been already evaluated
        self.desired_position_given = False
    

    def set_desired_position(self, desired_position):
        """ Sets the desired position the TBM will attempt to move to.
        
        Note: assume the user will pass in the desired_position parameter when using
        the interface 
        """
        self.desired_position = desired_position
        self.desired_position_given = False
        

    
    def update_current_position(self):
        """ Updates the current position of the TBM """
        self.GPS.pollSensor()
        self.current_position = self.GPS.getPos()
        


    def navigate(self):
        """ Navigate to the desired position from the current position
        
        Based on the current position tuple, compared to the desired position tuple,
        make decisions on steering, and ensure that the actuations are successful
        Returns: True if actuation requests were successful, False if not
        Note: It may be good to notify the user if something unexpected happens!
        """
        #checking if current postion and desired position are same and if same then prompting to input new values and calling navigate again
        #if both positions are same then we could either take new input and run navigate again like shown below or we could return an error status like the boolean values for actuatuion requests as mentioned above.
        if self.desired_position_given == False:
            if self.current_position == self.desired_position :
                print("TBM is already at desired position or desired position not set,please set new desired position \n")
                coordinate = input ("please input desired coordinate in the following form: ' x , y , z ' \n")
                #coordinate value taken at one go and then seperated as inputting the coordinates seperately will take longer time
                coordinate.replace(" ","")
                desired_coordinate_list = coordinate.split(",")
                desired_position_tuple = ()
                for number_of_coordinates in range(3):
                    updater_tuple = (desired_coordinate_list[number_of_coordinates],)
                    desired_position_tuple = desired_position_tuple + updater_tuple
                self.set_desired_position(desired_position_tuple)
                self.navigate
            #error checking for if the x given coordinate  is already behind the machine or not
            if self.current_position(0) > self.desired_position(0): 
                print("desired position for x axis is behind the TBM ,please put x coordinate which is infront of TBM \n")
                coordinate = input ("please input desired coordinate in the following form: ' x , y , z ' \n")
                coordinate.replace(" ","")
                desired_coordinate_list = coordinate.split(",")
                desired_position_tuple = ()
                for number_of_coordinates in range(3):
                    updater_tuple = (desired_coordinate_list[number_of_coordinates],)
                    desired_position_tuple = desired_position_tuple + updater_tuple
                self.set_desired_position(desired_position_tuple)
                self.navigate
            self.desired_position_given = True
        
        #differences between the coordinates is calculated
        difference_x = self.desired_position(0) - self.current_position(0)
        difference_y = self.desired_position(1) - self.current_position(1)
        difference_z = self.desired_position(2) - self.current_position(2)

        #checking each axis for which direction to move:front,right and above are taken to be positive while their opposite directions are taken as negative 
        #for the x axis
        if difference_x == 0:
            pass
        else:
            statusx = self.steering.move_forward()
            if statusx == False:
                print("error for forward moving actuator")
            #shouldn't the move_forward method also take the distance parameter?so that it hows how much to move forward
        #for x axis    
        if difference_y < 0 :
            statusy = self.steering.move_left(difference_y * (-1))
            if statusy == False:
                print("error is left moving actuator")
        elif difference_y > 0:
            statusy = self.steering.move_right(difference_y)
            if statusy == False:
                print("error is right moving actuator")
        else:
            pass
        #for the z axis
        if difference_z < 0 :
            statusz = self.steering.move_down(difference_z * (-1))
            if statusz == False:
                print("error in down moving actuator")
        elif difference_z > 0:
            statusz = self.steering.move_up(difference_z)
            if statusz == False :
                print("error in up moving actuator")
        else:
            pass
        #for stopping
        if difference_y == 0 and difference_x == 0 and difference_z == 0 and self.desired_position_given == True :
            status_stop = self.steering.stop()
            if status_stop == False:
                print("motor has not stopped")

    

        


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
    )
    
