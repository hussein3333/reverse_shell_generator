# reverse_shell_generator
Simple reverse shell generator

A Python-based reverse shell generator and listener. This tool can:
-Generate a reverse shell script tailored to your provided IP/ports.
-Start a listener to catch incoming reverse shells.

WARNING: This tool is intended for educational purposes and authorized security testing only. Unauthorized use may violate local and federal laws. Use responsibly.

Features:
-Automatic Reverse Shell Generation
-Dynamically creates a .py file that, when run on the target, connects back to your machine.
-Built-in Listener
-Spawns a TCP listener on your specified LHOST and LPORT to accept the reverse connection.
-Customizable Ports
-Specify which ports the victim will connect to (LPORT) 

Requirements
-Python 3.x (tested with Python 3.8+).
-A machine with network access to the target.
-No special Python libraries (beyond the standard library) are needed

Usage
-python reverse_shell_gen.py --lhost <ATTACKER_IP> --lport <ATTACKER_PORT>
