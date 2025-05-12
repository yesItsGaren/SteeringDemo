import can
import canmatrix
from canmatrix import CanMatrix, Frame, Signal
import os

# Configure the BLF file path
BLF_FILE = "example.blf"  # Change this to your actual BLF file
DBC_FILE = "example.dbc"  # Change this to your actual DBC file (optional)

def load_dbc(dbc_path):
    """Load the DBC file for decoding signals"""
    if os.path.exists(dbc_path):
        db = canmatrix.loadp(dbc_path)  # Load DBC
        print(f"Loaded DBC file: {dbc_path}")
        return db
    else:
        print("No DBC file found. Reading raw CAN data only.")
        return None

def read_blf_signals(blf_file, dbc_file=None):
    """Read and decode signals from a BLF file"""
    
    # Load the DBC file if provided
    dbc = load_dbc(dbc_file) if dbc_file else None
    
    # Open the BLF log file
    with can.BLFReader(blf_file) as log_reader:
        for msg in log_reader:
            print(f"Frame ID: {hex(msg.arbitration_id)}, Data: {msg.data.hex()}, Timestamp: {msg.timestamp:.6f}")

            # Decode the signals if a DBC file is available
            if dbc:
                can_frame_id = msg.arbitration_id
                if can_frame_id in dbc.frames:
                    frame = dbc.frames[can_frame_id]
                    signals = frame.decode(msg.data)
                    
                    # Print extracted signals
                    for signal_name, value in signals.items():
                        print(f"  Signal: {signal_name} = {value}")
                else:
                    print("  No matching frame found in DBC.")

if __name__ == "__main__":
    read_blf_signals(BLF_FILE, DBC_FILE)
