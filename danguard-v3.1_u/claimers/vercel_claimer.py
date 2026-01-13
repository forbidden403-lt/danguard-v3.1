import requests
from .base_claimer import BaseClaimer
from config import Config

class VercelClaimer(BaseClaimer):
    def __init__(self):
        super().__init__()
        self.headers = {
            "Authorization": f"Bearer {Config.VERCEL_API_KEY}",
            "Content-Type": "application/json"
        }

    def claim(self, target_name: str, **kwargs) -> dict:
        print(f"[*] Mencoba claim Vercel project: {target_name}")
        url = "https://api.vercel.com/v9/projects"
        payload = {"name": target_name, "framework": None}
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            if response.status_code in [200, 201]:
                return {'status': 'SUCCESS', 'claimed_resource': response.json()}
            elif response.status_code == 409:
                return {'status': 'TAKEN', 'reason': 'Nama project sudah digunakan.'}
            else:
                return {'status': 'PROTECTED', 'reason': f'Error {response.status_code}: {response.text}'}
        except Exception as e:
            return {'status': 'ERROR', 'reason': str(e)}