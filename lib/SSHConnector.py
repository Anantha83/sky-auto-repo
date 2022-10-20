from netmiko import ConnectHandler
import time


class SSHConnector():
    """
    Class contains methods that helps in connecting to device
    and configure/unconfigure/clear bgp
    """
    def __init__(self):
        self.handle = None
        self.device_type = None
        self.ip = None
        self.port = None
        self.user = None
        self.password = None
        self.secret = None
        
    @staticmethod
    def login(ip, device_type, port, username, password, secret):
        """
        Helps in login to the device

        :param ip: Ip used for connecting to device
        :param device_type: Currently supported cisco_ios future can
                            be used for other devices
        :param port: port used for connection, 22 for ssh
        :param username: username for login
        :param password: password to login
        :param secret: enable password login needed for configuration
        :return: return handler object on successful login
        """

        handle = ConnectHandler(
                        device_type=device_type,
                        host=ip,
                        port=port,
                        username=username,
                        password=password,
                        secret=secret
                 )
        return handle    

    @staticmethod
    def configure_bgp(handle, ip, local_as, remote_as, remote_ip, md5_pass):
        """
        Helps in configuring BGP

        :param handle: handler to connect to device
        :param ip: Ip used for connecting to device
        :param local_as: device ASN number
        :param remote_as: Remote ASN Number
        :param remote_ip: Router Neighbor IP
        :param md5_pass: MD5 Password

        :return:  configuration done on the device
        """

        handle.enable()
        
        config_commands = [f'router bgp {local_as}', 'bgp log-neighbor-changes', f'neighbor {remote_ip}\
         remote-as {remote_as}', f'neighbor {remote_ip} password {md5_pass}']
        
        sent_config = handle.send_config_set(config_commands)
        return sent_config

    @staticmethod
    def unconfigure_bgp(handle, ip, local_as):
        """
        Helps in unconfiguring BGP

        :param handle: handler to connect to device
        :param ip: Ip used for connecting to device
        :param local_as: device ASN number
        :return: configuration done on the device
        """
        handle.enable()
        config_commands = [f'no router bgp {local_as}']
        
        sent_config = handle.send_config_set(config_commands)
        return sent_config

    @staticmethod
    def verify_bgp(handle, ip, state=None):
        """
        Verify BGP is Active or connected based on State value

        :param handle: handler to connect to device
        :param ip: Ip used for connecting to device
        :param state: Success/Failure based on what has to be checked
        :return: raise exception to indicate problem if the state dont match
                 else returns bgp view output
        """

        handle.enable()
        retries = 5
        count = 0
        output = ""
        
        while (count < retries):
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
            # BGP sometime takes more time to form peering. Can be reduced by
            # increase polling interval
            time.sleep(10)
        return output

    @staticmethod
    def clear_bgp_session(handle, ip):
        """
        clears bgp session on router

        :param handle: handler to connect to device
        :param ip: Ip used for connecting to device
        :return: configuration done on the device
        """
        handle.enable()
        cmd = "clear ip bgp *"
        output = handle.send_command(cmd)
        time.sleep(2)
        return output
