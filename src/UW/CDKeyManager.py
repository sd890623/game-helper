# cdkey_manager.py
import platform
import requests
import hashlib
import wmi
import socket
import uuid
import datetime
from typing import Dict, Optional, Tuple

class CDKeyManager:
    def __init__(self):
        # self.api_base_url = "https://your-api-server.com/api"
        self.api_base_url = "http://127.0.0.1"

        self.machine_id = self._generate_machine_id()
        # Store cdkey in memory only during runtime
        self.cdkey = None
        
    def _generate_machine_id(self) -> str:
        """
        Generate a unique machine ID based on hardware information.
        Returns a hashed string of combined hardware details.
        """
        try:
            c = wmi.WMI()
            
            # Collect system information
            system_info = []
            
            # CPU information
            cpu_info = c.Win32_Processor()[0]
            system_info.append(str(cpu_info.ProcessorId).strip())
            
            # Motherboard information
            board_info = c.Win32_BaseBoard()[0]
            system_info.append(str(board_info.SerialNumber).strip())
            
            # Additional system identifiers
            system_info.extend([
                platform.node(),
                platform.machine(),
                str(uuid.getnode()),  # MAC address
                socket.gethostname()
            ])
            
            # Create a unique hash from the combined information
            combined_info = "".join(filter(None, system_info))
            return hashlib.sha256(combined_info.encode()).hexdigest()
            
        except Exception as e:
            print(f"Error generating machine ID: {e}")
            # Fallback to a basic machine ID if WMI fails
            fallback_id = f"{platform.node()}-{platform.machine()}-{uuid.getnode()}"
            return hashlib.sha256(fallback_id.encode()).hexdigest()
    
    def verify_key(self, cdkey: str) -> Tuple[bool, str]:
        """
        Verify the CDKey with the API server.
        Returns: (success: bool, message: str)
        """
        try:
            response = requests.post(
                f"{self.api_base_url}/verify",
                json={
                    "cdkey": cdkey,
                    "machine_id": self.machine_id
                },
                headers={
                    "Content-Type": "application/json"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("verified", True):
                    self.cdkey = cdkey  # Store key in memory only
                    return True, "验证成功"
                return False, result.get("message", "验证失败")
            
            return False, "服务器验证失败"
            
        except requests.exceptions.RequestException as e:
            return False, f"网络连接错误: {str(e)}"
        
    def _read_verification_data(self) -> Optional[Dict]:
        """
        Read stored verification data.
        """
        try:
            with open(self.verification_file, 'r') as f:
                data = json.load(f)
                if data.get('machine_id') == self.machine_id:
                    return data
                return None
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        
    def _check_local_verification(self) -> bool:
        """
        Fallback verification check using local data.
        """
        data = self._read_verification_data()
        if not data:
            return False
        
        expiry_date = data.get('expiry_date')
        if expiry_date:
            try:
                expiry = datetime.datetime.fromisoformat(expiry_date)
                if expiry < datetime.datetime.now():
                    return False
            except ValueError:
                return False
        
        return data.get('verified', False)
    def is_verified(self) -> bool:
        return True if self.cdkey else False
        """
        Check if the current installation is verified by checking with the API server.
        """
        if not self.cdkey:
            return False
            
        try:
            response = requests.post(
                f"{self.api_base_url}/check-status",
                json={
                    "cdkey": self.cdkey,
                    "machine_id": self.machine_id
                },
                headers={
                    "Content-Type": "application/json"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("verified", True):
                    return True, "验证成功"
                else:
                    self.cdkey = None  # Store key in memory only
                    return False, result.get("message", "验证失败")
            
            return False, "服务器验证失败"
            
        except requests.exceptions.RequestException:
            return False
    
    # def get_features(self) -> list:
    #     """
    #     Get list of features available for this license from the API.
    #     """
    #     if not self.cdkey:
    #         return []
            
    #     try:
    #         response = requests.get(
    #             f"{self.api_base_url}/features",
    #             params={
    #                 "cdkey": self.cdkey,
    #                 "machine_id": self.machine_id
    #             },
    #             timeout=10
    #         )
            
    #         if response.status_code == 200:
    #             result = response.json()
    #             return result.get("features", [])
            
    #         return []
            
    #     except requests.exceptions.RequestException:
    #         return []
    
    # def deactivate(self) -> Tuple[bool, str]:
    #     """
    #     Deactivate the current machine's license to allow activation on another machine.
    #     """
    #     if not self.cdkey:
    #         return False, "未激活的许可证"
            
    #     try:
    #         response = requests.post(
    #             f"{self.api_base_url}/deactivate",
    #             json={
    #                 "cdkey": self.cdkey,
    #                 "machine_id": self.machine_id
    #             },
    #             headers={
    #                 "Content-Type": "application/json"
    #             },
    #             timeout=10
    #         )
            
    #         if response.status_code == 200:
    #             result = response.json()
    #             if result.get("success", False):
    #                 self.cdkey = None
    #                 return True, "许可证已停用"
    #             return False, result.get("message", "停用失败")
            
    #         return False, "服务器处理失败"
            
    #     except requests.exceptions.RequestException as e:
    #         return False, f"网络连接错误: {str(e)}"

# Example expected API responses:
"""
/verify response:
{
    "verified": true,
    "message": "验证成功",
    "features": ["feature1", "feature2"]
}

/check-status response:
{
    "verified": true,
    "message": "验证成功",
}

/features response:
{
    "features": ["feature1", "feature2", "feature3"]
}

/deactivate response:
{
    "success": true,
    "message": "许可证已停用"
}
"""