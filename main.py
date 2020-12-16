import os, sys, inspect, argparse, collections, time, random, enum
import scripts.Util

def load_modules_from_path(path):
    """
    Import all modules from the given directory
    """
    
    imported_modules = []
    # Check and fix the path
    if path[-1:] != '/':
        path += '/'

    # Get a list of files in the directory, if the directory exists
    if not os.path.exists(path):
        path = os.path.dirname(os.path.realpath(__file__)) + "/" + path
        if not os.path.exists(path):
            raise OSError("Directory does not exist: %s" % path)
    
    # Add path to the system path
    sys.path.append(path)
    # Load all the files in path
    for f in os.listdir(path):
        # Ignore anything that isn't a .py file
        if len(f) > 3 and f[-3:] == '.py' and f != 'Util.py':
            modname = f[:-3]
            # Import the module
            __import__(modname, globals(), locals(), ['*'])
            imported_modules.append(modname)
    return imported_modules

def load_class_from_name(fqcn):
    # Break apart fqcn to get module and classname
    paths = fqcn.split('.')
    modulename = '.'.join(paths[:-1])
    classname = paths[-1]
    # Import the module
    __import__(modulename, globals(), locals(), ['*'])
    # Get the class
    cls = getattr(sys.modules[modulename], classname)
    # Check cls
    if not inspect.isclass(cls):
       raise TypeError("%s is not a class" % fqcn)
    # Return class
    return cls

def is_valid_exploit_class(class_object):
    found_invalid_class = False
    # Check if every required metadata piece exists.
    required_attributes = ["Name", "Description", "Author", "Type", "Platform", "Version", "run" , "POC", "HOST", "PORT"]
    for attribute in required_attributes:
        if attribute not in dir(class_object):
            print(f"The file {class_object.__module__}.py is missing the {attribute} attribute.")
            found_invalid_class = True   
    
    # Check if the attribute types are an enum type so we 
    enum_type_attributes = ["Platform", "Type"]
    for attr in enum_type_attributes:
        if(not issubclass(type(getattr(class_object,attr)),enum.Enum)):
            print(f"The attribute {attr} is not an enum. Please use the enum to keep consistancy.")
            found_invalid_class = True   

    return not found_invalid_class

def get_all_classes():
    # Import & return every class object inside the scripts folder.

    exploit_classes = []

    modules = load_modules_from_path("scripts")
    for module in modules:
        for _, module_member in inspect.getmembers(sys.modules[module]):
            # If the member inside the
            if inspect.isclass(module_member):
                # Instanciate the class & Validate it.
                possible_exploit = module_member()
                if(not is_valid_exploit_class(possible_exploit)):
                    print(f"Please solve the above mentioned problems.")
                    exit(1)
                
                # Validate duplicate names
                for exploit in exploit_classes:
                    if exploit.Name == possible_exploit.Name:
                        print(f"There are two exploit classes with the same Name attribute ({possible_exploit.Name}), please keep these unique.")
                        exit(1)
                # Add the exploit class to the list of valid exploits.
                exploit_classes.append(possible_exploit)

    return exploit_classes

def automated_attacks(exploit_classes):
    while True:
        print("Picking an exploit")
        time.sleep(random.randint(10,100))
        picked_exploit = random.choice(exploit_classes)
        print(f"Picked: {picked_exploit.Name}")
        if(picked_exploit.Type == Util.Type.Local):
            # Run a shell first. 
            pass

        



def main():
    exploit_classes = get_all_classes()


    parser = argparse.ArgumentParser(description="The management script of the red team attack framework.")
    group = parser.add_mutually_exclusive_group()

    # Pack the options that can only exist one of, these are the different modes.
    group.add_argument('-a','--automate',action="store_true", help='automate the attack framework')
    group.add_argument('-p','--payload', action='store', type=str, help='The text to parse.')
    group.add_argument('-d','--details',action="store_true" , help="Print every exploits' details.")
    group.add_argument('-l','--list', action='store_true', help="List every exploit name only")
    # Pack the optional parameters.
    parser.add_argument('--host', help="The host to execute the payload on.")
    parser.add_argument('--port',type=int , help="The port to execute the payload on.")
    
    
    # Parse the arguments to a namespace.
    args = parser.parse_args()

    # Print the arguments
    print(args)

    # Print the metadata information of every exploit.
    if(args.details):
        for exploit in exploit_classes:
            print(f"Name: {exploit.Name}")
            print(f"Description: {exploit.Description}")
            print(f"Author: {exploit.Author}")
            print(f"Version: {exploit.Version}")
            print(f"Proof Of Concept: {exploit.POC}")
            print()
        exit(0)

    if(args.list):
        for exploit in exploit_classes:
            print(exploit.Name)
        exit(0)
    
    # Run the script in automated mode.
    if args.automate:
        automated_attacks(exploit_classes)
        exit(0)

    # Run the script in payload mode.
    selected_exploit = None

    # Check if there is an exploit with the given payload name.
    for exploit in exploit_classes:
        if(exploit.Name == args.payload):
            selected_exploit = exploit

    if selected_exploit == None:
        print("The payload is not known, keep in mind the case sensitivity.")
        print("The list of known payloads is:")
        for exploit in exploit_classes:
            print(f"{exploit.Name}")
        exit(1)
    
    # If the host option is given set it to the current exploit.
    if(args.host != None):
        selected_exploit.HOST = args.host
    
    # If the port option is given set it to the current exploit.
    if(args.port != None):
        selected_exploit.PORT = args.port
    
    # Execute the exploit.
    selected_exploit.run()
    

if __name__ == '__main__': 
    main()
