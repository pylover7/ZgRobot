from datetime import datetime
from zgrobot.logger import zglogger

tody = datetime.now().strftime("%Y-%m-%d")

def test_debug():
    zglogger.debug("Test debug message")
    with open(f"log/{tody}.log", "r") as f:
        lines = f.readlines()
        assert lines[-1].split(" | ")[-2] == "DEBUG"
        assert lines[-1].split(" | ")[-1][:-1] == "Test debug message"
        
def test_info():
    zglogger.info("Test info message")
    with open(f"log/{tody}.log", "r") as f:
        lines = f.readlines()
        assert lines[-1].split(" | ")[-2] == "INFO"
        assert lines[-1].split(" | ")[-1][:-1] == "Test info message"
        
def test_warning():
    zglogger.warning("Test warning message")
    with open(f"log/{tody}.log", "r") as f:
        lines = f.readlines()
        assert lines[-1].split(" | ")[-2] == "WARNING"
        assert lines[-1].split(" | ")[-1][:-1] == "Test warning message"

def test_error():
    zglogger.error("Test error message")
    with open(f"log/{tody}.log", "r") as f:
        lines = f.readlines()
        assert lines[-1].split(" | ")[-2] == "ERROR"
        assert lines[-1].split(" | ")[-1][:-1] == "Test error message"
        
def test_critical():
    zglogger.critical("Test critical message")
    with open(f"log/{tody}.log", "r") as f:
        lines = f.readlines()
        assert lines[-1].split(" | ")[-2] == "CRITICAL"
        assert lines[-1].split(" | ")[-1][:-1] == "Test critical message"
