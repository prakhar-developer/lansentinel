# __main__.py

from cli.admin_panel import run_admin_cli
import logging
import os

def setup_logging():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "lansentinel.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("LANSentinel++ system initialized.")

if __name__ == "__main__":
    setup_logging()
    try:
        print("🚀 Launching LANSentinel++ Admin CLI Panel...")
        run_admin_cli()
    except KeyboardInterrupt:
        print("\n🛑 Exiting LANSentinel++")
        logging.info("System shutdown via KeyboardInterrupt.")
