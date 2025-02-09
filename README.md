# reverse_shell_generator
Simple reverse shell generator

A Python-based reverse shell generator and listener. This tool can:
</br>-Generate a reverse shell script tailored to your provided IP/ports.
</br>-Start a listener to catch incoming reverse shells.

WARNING: This tool is intended for educational purposes and authorized security testing only. Use responsibly!

Features:
</br>-Automatic Reverse Shell Generation
</br>-Dynamically creates a .py file that, when run on the target, connects back to your machine.
</br>-Built-in Listener
</br>-Spawns a TCP listener on your specified LHOST and LPORT to accept the reverse connection.
</br>-Specify which ports the victim will connect to (LPORT) 

Requirements
</br>-Python 3.x (tested with Python 3.8+).
</br>-A machine with network access to the target.
</br>-No special Python libraries (beyond the standard library) are needed

Usage
</br>-python reverse_shell_gen.py --lhost <ATTACKER_IP> --lport <ATTACKER_PORT>
