def calculate():
    unknown = raw_input("What are you trying to find? Type 'f' for force, 'm' for mass, or 'a' for acceleration. \n")
    if unknown == "f":
        mass = float(raw_input("Enter Mass in Kg\n"))
        acceleration = float(raw_input("Enter Acceleration in m/s^2\n"))
        force = mass * acceleration
        print "Force = " + str(force) + " Newtons\n"
    elif unknown == "m":        
        acceleration = float(raw_input("Enter Acceleration in m/s^2.\n"))
        force = float(raw_input("Enter Force in Newtons.\n"))
        mass = force / acceleration
        print "Mass = " + str(mass) + " Kg"
    elif unknown == "a":
        force = float(raw_input("Enter Force in Newtons.\n"))
        mass = float(raw_input("Enter Mass in Kg\n"))
        acceleration = force/mass
        print "Acceleration = " + str(acceleration) + " m/s^2\n"
    else:
        print "You didn't choose f,m,or a... Please try again."
