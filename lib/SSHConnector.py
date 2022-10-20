from netmiko import ConnectHandler
import time

class SSHConnector():
    
    def __init__(self):
        self.handle = None
        self.device_type = None
        self.ip = None
        self.port = None
        self.user = None
        self.password = None
        self.secert = None
        
    def login(self, ip, device_type, port, username, password, secret):
        
        handle = ConnectHandler(
                        device_type = device_type,
                        host = ip,
                        port = port ,
                        username = username,
                        password = password,
                        secret = secret
                 )
        return handle    
            
    
    def configure_bgp(self, handle, ip, local_as, remote_as, remote_ip, md5_pass):
        
        handle.enable()
        
        config_commands = [f'router bgp {local_as}', 'bgp log-neighbor-changes', f'neighbor {remote_ip} remote-as {remote_as}', f'neighbor {remote_ip} password {md5_pass}']
        
        sentConfig = handle.send_config_set(config_commands)
        return sentConfig
      
    def unconfigure_bgp(self, handle, ip, local_as):
        handle.enable()
        
        cmd = "show ip int bri"
        sentConfig = handle.send_command(cmd)
        config_commands = [f'no router bgp {local_as}']
        
        sentConfig = handle.send_config_set(config_commands)
        return sentConfig 
        

    def verify_bgp(self, handle, ip, state=None):
        handle.enable()
        retries = 5
        count = 0
        
        while ( count < retries):
            cmd = "show ip bgp summ"
            
            output = handle.send_command(cmd)
            
            if "BGP not active" in output:
                if count >= retries:
                    raise Exception(f"BGP not Configured : {output}")
            if state == "Success":                
                   if "Active" in output:
                        if count >= retries: 
                            raise Exception(f"BGP Peering not formed : {output}") 
            if state == "Failure":
                    if "Active" not in output:
                        if count >= retries:
                            raise Exception(f"BGP Peering is active which is not expected in this condition : {output}") 
            count = count + 1 
            time.sleep(10)
        return output
        
    def clear_bgp_session(self, handle, ip):
        handle.enable()
        
        cmd = "clear ip bgp *"
        
        output = handle.send_command(cmd) 
        
        time.sleep(2)
        
        return output
        
        
        
        
        
    


            
         
   

