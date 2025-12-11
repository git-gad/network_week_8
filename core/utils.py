import ipaddress

def get_valid_ip():
     while True:
         ip = input("input ip (in format x.x.x.x): ")
         try:
            ipaddress.IPv4Address(ip) #Create IPv4Address object
            return ip
         except ValueError:
            print("not valid ip")
    

def get_valid_mask():
    while True:
        mask = input("input mask (in format 255.255.255.0): ")
        try:
            ipaddress.IPv4Network(f"0.0.0.0/{mask}") #Check mask on sample IP
            return mask
        except ValueError:
            print("not valid")

    


