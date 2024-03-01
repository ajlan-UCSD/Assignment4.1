import socket
import multiprocessing
def client_process():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('PYNQ_Z2_IP', 9999))  # Replace 'PYNQ_Z2_IP' with the actual IP address of the PYNQ-Z2 board

    # Send commands to trigger actions on the server
    # (e.g., send signal to emit tone)
    # client_socket.sendall(data)

    client_socket.close()
if __name__ == '__main__':
    client_proc = multiprocessing.Process(target=client_process)
    client_proc.start()
