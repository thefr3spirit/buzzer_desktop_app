# desktop_app/serial_thread.py
from PyQt5.QtCore import QThread, pyqtSignal
import serial
import time

class SerialThread(QThread):
    buzzReceived = pyqtSignal(str)  # Signal to send received messages to the UI

    def __init__(self, port, baudrate=115200, parent=None):
        super().__init__(parent)
        self.port = port
        self.baudrate = baudrate
        self._running = True

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except Exception as e:
            print("Could not open serial port", self.port, e)
            return

        while self._running:
            try:
                if ser.in_waiting:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        self.buzzReceived.emit(line)
                else:
                    # Sleep briefly to reduce CPU usage
                    time.sleep(0.1)
            except Exception as e:
                print("Serial read error:", e)
                time.sleep(0.1)
        ser.close()

    def stop(self):
        self._running = False
