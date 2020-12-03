# AutomatedAttackScript

The purpose of this script is to simulate attacks on the vulnerable part of the network.
The exploits are written modular so if you want to add more attacks just write a class in the scripts folder.
This script will validate every exploit so if there are missing parameters it will tell you.

# Installation
To install the required libraries run
`python -m pip install -r requirements.txt`

# Usage
For normal usage
`python main.py -p <payload name> --host <host ip address> --port <port>`

For more information about every parameter
`python main.py --help`

