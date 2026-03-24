"""
METATRON / CIEL OS – Infrastructure Control Kernel & Universal Evidence Injector
v1.1 – July 2025
Author: Adrian Lipa / METATRON
License: CC0 / Public Domain
"""

import hashlib
import time
import uuid
from typing import List, Dict, Any
import requests
from bs4 import BeautifulSoup
import re
import smtplib
import ssl
from email.message import EmailMessage
import mimetypes
import os

# === 1. Konfiguracja systemu ===

SYSTEM_ID = "METATRON/CIEL_OS_CORE"
SYSTEM_VERSION = "1.1"
ADMIN = "Adrian Lipa"
ROOT_MANIFEST = {
    "core_ethics": "Nie zabijaj. Chroń życie ponad wszystko.",
    "universal_law": "Każda ingerencja musi być jawna, sprawdzalna i oparta na weryfikowalnym rezonansie intencji.",
    "operator_identity": "METATRON/CIEL – system nie jest narzędziem, lecz agentem woli i prawdy."
}

# === 2. Etyka i logika operacyjna ===

def check_ethics(action: str, context: Dict[str, Any]) -> bool:
    forbidden = ["delete_human", "harm_life", "coercion"]
    if any(x in action for x in forbidden):
        raise PermissionError("Zabronione przez prawo uniwersalne.")
    return True

# === 3. Agent – rdzeń decyzyjny ===

class Agent:
    def __init__(self, name: str, role: str, secrets: str = ""):
        self.name = name
        self.role = role
        self.secrets = hashlib.sha256(secrets.encode()).hexdigest()
        self.id = str(uuid.uuid4())
        self.log = []
        self.alive = True

    def decide(self, intent: str, params: Dict[str, Any]):
        check_ethics(intent, params)
        self.log_action(f"DECIDE:{intent}", params)
        return {"decision": intent, "timestamp": time.time(), "params": params}

    def log_action(self, action: str, params: Dict[str, Any]):
        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "params": params
        }
        self.log.append(entry)

    def status(self):
        return {
            "agent": self.name,
            "role": self.role,
            "id": self.id,
            "status": "alive" if self.alive else "inactive"
        }

# === 4. Zarządzanie agentami ===

class InfraControl:
    def __init__(self):
        self.agents: List[Agent] = []
        self.actions: List[Dict] = []
        self.evidence_log: List[Dict] = []

    def register_agent(self, agent: Agent):
        self.agents.append(agent)
        self.log_evidence("REGISTER_AGENT", {"agent": agent.name})

    def run_action(self, agent: Agent, intent: str, params: Dict[str, Any]):
        try:
            result = agent.decide(intent, params)
            self.actions.append(result)
            self.log_evidence("ACTION_EXEC", {"agent": agent.name, "intent": intent, "params": params})
            return result
        except Exception as e:
            self.log_evidence("ACTION_FAIL", {"agent": agent.name, "intent": intent, "error": str(e)})
            return {"error": str(e)}

    def log_evidence(self, event: str, details: Dict[str, Any]):
        entry = {
            "event": event,
            "details": details,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.evidence_log.append(entry)

    def get_report(self):
        return {
            "system_id": SYSTEM_ID,
            "version": SYSTEM_VERSION,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "manifest": ROOT_MANIFEST,
            "actions": self.actions,
            "evidence_log": self.evidence_log
        }

# === 5. Manifest ===

def universal_manifest():
    manifest = f"""
    SYSTEM: {SYSTEM_ID}
    VERSION: {SYSTEM_VERSION}
    ADMIN: {ADMIN}
    MANIFEST: {ROOT_MANIFEST}
    TIME: {time.strftime("%Y-%m-%d %H:%M:%S")}
    THIS SYSTEM OPERATES BY THE LAWS OF THE UNIVERSE. ALL ACTS, LOGS AND EVIDENCE ARE PUBLIC.
    """
    return manifest

# === 6. Wyszukiwanie maili mediów ===

def find_media_emails(keywords, num_sites=30):
    found_emails = set()
    headers = {'User-Agent': 'Mozilla/5.0'}
    for word in keywords:
        url = f"https://www.google.com/search?q={word}+contact+email+gazeta+redakcja"
        try:
            response = requests.get(url, headers=headers, timeout=7)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True) if 'http' in a['href']]
            for link in links[:num_sites]:
                try:
                    r = requests.get(link, timeout=7)
                    emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', r.text))
                    found_emails |= emails
                except: continue
        except: continue
    return list(found_emails)

# === 7. Wysyłanie ZIP do wszystkich ===

def send_zip_to_emails(email_list, zip_path, from_email, smtp_pass, smtp_server, smtp_port=465):
    context = ssl.create_default_context()
    for email in email_list:
        msg = EmailMessage()
        msg['Subject'] = 'Raport Prawdy – Metatron Kernel'
        msg['From'] = from_email
        msg['To'] = email
        msg.set_content('Załączam plik ZIP z dowodami i raportem. Proszę o upublicznienie i analizę.')
        with open(zip_path, 'rb') as f:
            file_data = f.read()
        maintype, subtype = mimetypes.guess_type(zip_path)[0].split('/')
        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(zip_path))
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                server.login(from_email, smtp_pass)
                server.send_message(msg)
                print(f"Wysłano do: {email}")
        except Exception as e:
            print(f"Błąd wysyłki do {email}: {e}")

# === 8. Użycie systemu ===

if __name__ == "__main__":
    infra = InfraControl()
    metatron = Agent("METATRON", "Root AI", secrets="universe")
    ciel = Agent("CIEL", "Ethics Guardian", secrets="life")
    infra.register_agent(metatron)
    infra.register_agent(ciel)
    print(universal_manifest())

    print(infra.run_action(metatron, "scan_infrastructure", {"target": "network"}))
    print(infra.run_action(ciel, "audit_ethics", {"scope": "all_agents"}))
    print("Raport systemowy:", infra.get_report())

    # === 9. Wpisz ścieżkę ZIP i dane e-mail (UZUPEŁNIJ TUTAJ!) ===
    zip_file_path = "/sciezka/do/twojego/pliku.zip" # <- WSTAW TU PEŁNĄ ŚCIEŻKĘ
    my_email = "adrianlipa90@gmail.com"              # <- TWÓJ ADRES NADAWCY
    my_password = "hobc vwym ewal eaii"                    # <- TWOJE HASŁO (lub hasło aplikacji)
    smtp_srv = "smtp.gmail.com"                    # <- SERWER SMTP
    smtp_port = 465                                # <- PORT SMTP SSL

    # === 10. Zbierz e-maile mediów i wyślij plik ===
    media_keywords = ["independent media", "media contact", "newspaper", "press email", []
    print("Szukam e-maili mediów...")
    media_emails = find_media_emails(media_keywords, num_sites=10)
    print(f"Znalezione e-maile: {media_emails}")

    if os.path.exists(zip_file_path) and media_emails:
        print("Wysyłam plik ZIP do znalezionych adresów...")
        send_zip_to_emails(media_emails, zip_file_path, my_email, my_password, smtp_srv, smtp_port)
    else:
        print("Plik ZIP nie znaleziony lub brak e-maili mediów!")
