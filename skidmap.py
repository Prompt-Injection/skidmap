import os
import random

def print_welcome_banner():
    """
    Prints a welcome banner with the program name and author.
    """
    banner = r"""
 _____                                                     _____ 
( ___ )                                                   ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____    _      _       _   __  __                  |   | 
 |   | / ___|  | | __ (_)   __| | |  \/  |   __ _   _ __   |   | 
 |   | \___ \  | |/ / | |  / _` | | |\/| |  / _` | | '_ \  |   | 
 |   |  ___) | |   <  | | | (_| | | |  | | | (_| | | |_) | |   | 
 |   | |____/  |_|\_\ |_|  \__,_| |_|  |_|  \__,_| | .__/  |   | 
 |   |                                             |_|     |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                   (_____)
    """
    print(banner)
    print("\nAuthor: Prompt Injection\n")
    print("""
[*] Welcome to SkidMap! 
[*] This tool is designed to automate those tedious Nmap commands, making network scanning faster and more efficient.
[*] Whether you're a Penetration tester or a Blue Teamer, SkidMap will guide you through the powerful world of Nmap.
[*] With built-in explanations of various flags and options, you'll not only streamline your scans but also gain valuable insights into how Nmap operates.
[*] With SkidMap Network Reconnaissance haven't been easier, Happy Hacking! \n""")

def phase_one_ping_sweep(target):
    """
    Performs a ping sweep using ARP ping and gives option to save live hosts.
    """
    print(f"[*] Starting Phase One: Ping Sweep on {target}")
    print("""
    Explanation of flags used in the ping sweep:
    -sn : Ping scan, do not perform a port scan.
    -PR : ARP requests will be used for pinging the target (effective on local networks).
    -oG : Outputs results in a greppable format.
    - | awk '/Up$/{print $2}}' : Filters and extracts live hosts.
    """)

    try:
        command = f"nmap -sn -PR {target} -oG - | awk '/Up$/{{print $2}}' > hosts.txt"
        os.system(command)
        
        # Check if hosts.txt exists
        if os.path.exists("hosts.txt"):
            with open("hosts.txt", "r") as file:
                live_hosts = file.readlines()
                if live_hosts:
                    print("[+] Hosts found during ping sweep:")
                    for host in live_hosts:
                        print(f"    Host: {host.strip()}")

                    # Ask the user if they want to save live hosts for future use
                    save_choice = input("\nDo you want to save live hosts to a file for future scans? (y/n): ")
                    if save_choice.lower() == 'y':
                        filename = input("Enter the filename to save live hosts (without extension): ")
                        with open(f"{filename}.txt", "w") as save_file:
                            save_file.writelines(live_hosts)
                        print(f"[+] Live hosts saved to {filename}.txt")
                    return live_hosts
                else:
                    print("[-] No hosts responded to the ping sweep.")
                    return None
        else:
            print("[-] hosts.txt file was not created. Something went wrong.")
            return None
    except Exception as e:
        print(f"[!] Error running ping sweep: {str(e)}")
        return None

def save_scan_results(scan_command, filename=None, output_format=None):
    """
    Executes the scan command and saves the results if filename is provided.
    """
    if filename and output_format:
        if output_format == '1':
            scan_command += f" -oN {filename}.txt"  # Normal output
        elif output_format == '2':
            scan_command += f" -oX {filename}.xml"  # XML output
    
    os.system(scan_command)

def basic_port_scan(hosts_file, output_format, filename):
    """
    Basic scan for service versions and OS detection (-sV -O).
    """
    print(f"\n[*] Running Basic Port Scan on hosts listed in {hosts_file}")
    print("""
    Explanation of flags used in the Basic Port Scan:
    -sV : Probe open ports to determine service/version info.
    -O : Enable OS detection.
    -iL : Input from list of hosts in the specified file.
    """)
    scan_command = f"nmap -sV -O -iL {hosts_file}"
    save_scan_results(scan_command, filename, output_format)

def port_sweep_basic_scan(target, ports, output_format, filename):
    """
    Port sweep basic scan for service versions and OS detection specifying ports (-sV -O -p).
    """
    print(f"\n[*] Running Port Sweep Basic Scan on target {target} for ports: {ports}")
    print("""
    Explanation of flags used in the Port Sweep Basic Scan:
    -sV : Probe open ports to determine service/version info.
    -O : Enable OS detection.
    -p : Specifies which ports to scan.
    """)
    scan_command = f"nmap -sV -O -p {ports} {target}"
    save_scan_results(scan_command, filename, output_format)

def stealthy_scan(hosts_file, output_format, filename):
    """
    Stealthy scan with firewall evasion techniques (-g 53 -mtu 16) and changing source MAC address.
    """
    random_mac = f"00:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}"
    print(f"\n[*] Running Stealthy Scan on hosts listed in {hosts_file} with firewall evasion techniques (Source MAC: {random_mac})")
    print("""
    Explanation of flags used in the Stealthy Scan:
    -g 53 : Use source port 53 (DNS) for the scan, which can help in evading firewalls.
    --mtu 16 : Set the Maximum Transmission Unit (MTU) for packets to make them smaller and less detectable.
    -iL : Input from list of hosts in the specified file.
    """)
    scan_command = f"nmap -g 53 --mtu 16 -iL {hosts_file}"
    save_scan_results(scan_command, filename, output_format)

def port_sweep_stealthy_scan(target, ports, output_format, filename):
    """
    Stealthy port sweep scan specifying ports with firewall evasion techniques.
    """
    random_mac = f"00:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}"
    print(f"\n[*] Running Stealthy Port Sweep Scan on target {target} for ports: {ports} (Source MAC: {random_mac})")
    print("""
    Explanation of flags used in the Stealthy Port Sweep Scan:
    -g 53 : Use source port 53 (DNS) for the scan to help evade detection by firewalls.
    --mtu 16 : Set the Maximum Transmission Unit (MTU) for smaller packets to reduce detection likelihood.
    -p : Specifies which ports to scan.
    """)
    scan_command = f"nmap -g 53 --mtu 16 -p {ports} {target}"
    save_scan_results(scan_command, filename, output_format)

def aggressive_scan(hosts_file, output_format, filename):
    """
    Aggressive scan with OS detection, version detection, and traceroute (-A).
    """
    print(f"\n[*] Running Aggressive Scan on hosts listed in {hosts_file}")
    print("""
    Explanation of flags used in the Aggressive Scan:
    -A : Enable OS detection, version detection, script scanning, and traceroute.
    -T4 : Set timing template for faster execution (aggressive).
    -iL : Input from list of hosts in the specified file.
    """)
    scan_command = f"nmap -A -T4 -iL {hosts_file}"
    save_scan_results(scan_command, filename, output_format)

def port_sweep_aggressive_scan(target, ports, output_format, filename):
    """
    Aggressive port sweep scan specifying ports.
    """
    print(f"\n[*] Running Aggressive Port Sweep Scan on target {target} for ports: {ports}")
    print("""
    Explanation of flags used in the Aggressive Port Sweep Scan:
    -A : Enable OS detection, version detection, script scanning, and traceroute.
    -T4 : Set timing template for faster execution (aggressive).
    -p : Specifies which ports to scan.
    """)
    scan_command = f"nmap -A -T4 -p {ports} {target}"
    save_scan_results(scan_command, filename, output_format)

def custom_nmap_scan():
    """
    Custom Nmap scan based on user input.
    """
    # Allow the user to enter the full Nmap command directly
    custom_command = input("Enter your custom Nmap command: ")
    
    print(f"\n[*] Running Custom Nmap Scan: {custom_command}")
    
    # Ask the user if they want to save the results
    save_choice = input("Do you want to save the scan results to a file? (y/n): ")
    if save_choice.lower() == 'y':
        output_choice = input("""
Do you want the scan results saved in:
1. Normal output (-oN)
2. XML output (-oX)
Enter your choice (1 or 2): """)

        if output_choice not in ['1', '2']:
            print("[!] Invalid option selected. Defaulting to Normal Output.")
            output_choice = '1'

        # Ask for the filename to save the scan results
        filename = input("Enter the filename to save scan results (without extension): ")
        save_scan_results(custom_command, filename, output_choice)
    else:
        os.system(custom_command)

def display_scan_options(port_sweep=False):
    """
    Displays scanning options for the user.
    """
    print("\nChoose a scanning option:")
    print("1. Basic Port Scan (Service and OS Detection)")
    if not port_sweep:
        print("2. Stealthy Scan with Firewall Evasion Techniques")
        print("3. Aggressive Scan (Comprehensive with OS Detection)")
    else:
        print("2. Stealthy Port Sweep Scan with Firewall Evasion Techniques")
        print("3. Aggressive Port Sweep Scan (Comprehensive with OS Detection)")

def main():
    print_welcome_banner()  # Print the welcome banner
    
    while True:
        print("\nChoose an option:")
        print("1. Ping Sweep Scan (Recommended)")
        print("2. Port Sweep (Targeted)")
        print("3. Custom Nmap Scan (Advanced)")  # Custom Nmap Scan option
        
        mode_choice = input("Enter your choice (1, 2, 3): ")
        
        if mode_choice == "1":
            target = input("\nEnter target IP(s) or range (e.g., 192.168.1.0/24) for ping sweep: ")
            live_hosts = phase_one_ping_sweep(target)
            
            if live_hosts:
                # Now, perform the scan based on the user's choice
                display_scan_options()
                choice = input("Enter your choice (1-3): ")

                # Ask for the output format and filename after selecting the scan option
                output_choice = input("""
Do you want the scan results saved in:
1. Normal output (-oN)
2. XML output (-oX)
Enter your choice (1 or 2): """)

                # Set the output format based on user choice
                if output_choice not in ['1', '2']:
                    print("[!] Invalid option selected. Defaulting to Normal Output.")
                    output_choice = '1'

                # Ask for the filename to save the scan results
                filename = input("Enter the filename to save scan results (without extension): ")

                # Call the appropriate scan function without port specifications
                if choice == "1":
                    basic_port_scan("hosts.txt", output_choice, filename)
                elif choice == "2":
                    stealthy_scan("hosts.txt", output_choice, filename)
                elif choice == "3":
                    aggressive_scan("hosts.txt", output_choice, filename)                   
                else:
                    print("[!] Invalid option. Please try again.")

            else:
                print("[!] No live hosts to scan. Try again.")
        
        elif mode_choice == "2":
            target = input("\nEnter target IP(s) or range (e.g., 192.168.1.0/24) for port sweep: ")
            print(f"[*] You selected target: {target}.")
            
            # Now, perform the scan based on the user's choice (no hosts.txt file creation)
            display_scan_options(port_sweep=True)
            choice = input("Enter your choice (1-3): ")

            # Ask for the output format and filename for the port sweep
            output_choice = input("""
Do you want the scan results saved in:
1. Normal output (-oN)
2. XML output (-oX)
Enter your choice (1 or 2): """)

            # Set the output format based on user choice
            if output_choice not in ['1', '2']:
                print("[!] Invalid option selected. Defaulting to Normal Output.")
                output_choice = '1'

            filename = input("Enter the filename to save scan results (without extension): ")
            ports = input("Enter the ports to scan (e.g., 22,80,443): ")  # Asking for ports

            # Call the appropriate scan function for port sweeps
            if choice == "1":
                port_sweep_basic_scan(target, ports, output_choice, filename)
            elif choice == "2":
                port_sweep_stealthy_scan(target, ports, output_choice, filename)
            elif choice == "3":
                port_sweep_aggressive_scan(target, ports, output_choice, filename)
            else:
                print("[!] Invalid option. Please try again.")

        elif mode_choice == "3":
            # Custom Nmap Scan option
            custom_nmap_scan()

        else:
            print("[!] Invalid option. Please try again.")
        
        continue_choice = input("\nDo you want to perform another operation? (y/n): ")
        if continue_choice.lower() != 'y':
            print("[*] Exiting SkidMap. Goodbye!")
            break

if __name__ == "__main__":
    main()
