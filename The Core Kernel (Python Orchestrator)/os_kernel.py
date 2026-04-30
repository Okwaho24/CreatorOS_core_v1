import os
import json
import logging
from pathlib import Path

class CreatorOSKernel:
    def __init__(self):
        self.root = Path(__file__).parent
        self.config = self._load_manifest()
        self._setup_logging()

    def _load_manifest(self):
        with open(self.root / "manifest.json", "r") as f:
            return json.load(f)

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='[CreatorOS-Kernel] %(asctime)s - %(levelname)s - %(message)s'
        )

    def verify_engines(self):
        """Checks for the presence of AcerbE and RaPaX in the local environment."""
        engines = self.config.get("engine_hooks", {})
        for name, engine in engines.items():
            # Logic to check for local engine directories
            status = "FOUND" if (self.root.parent / name.lower()).exists() else "MISSING"
            logging.info(f"Engine {engine}: {status}")

    def boot(self):
        logging.info(f"Booting {self.config['system']} v{self.config['version']}...")
        self.verify_engines()
        logging.info("Sovereign Environment Stable.")

if __name__ == "__main__":
    os_kernel = CreatorOSKernel()
    os_kernel.boot()
  
