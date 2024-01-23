from googleapiclient import discovery
import google.oauth2.service_account
from google.oauth2.credentials import Credentials
import os
import sys
import time
import argparse
from googleapiclient.errors import HttpError
from permissions import permissions

def print_banner():
    banner = """
                        ('-.       .-') _             _   .-')    
                      _(  OO)     ( OO ) )           ( '.( OO )_  
  ,----.             (,------.,--./ ,--,' ,--. ,--.   ,--.   ,--.)
 '  .-./-')    .-')   |  .---'|   \ |  |\ |  | |  |   |   `.'   | 
 |  |_( O- ) _(  OO)  |  |    |    \|  | )|  | | .-') |         | 
 |  | .--, \(,------.(|  '--. |  .     |/ |  |_|( OO )|  |'.'|  | 
(|  | '. (_/ '------' |  .--' |  |\    |  |  | | `-' /|  |   |  | 
 |  '--'  |           |  `---.|  | \   | ('  '-'(_.-' |  |   |  | 
  `------'            `------'`--'  `--'   `-----'    `--'   `--' 
    By Joey Joseph
    """
    print(banner)

def print_animated_message(message, delay=0.1):
    for i in range(3):
        sys.stdout.write(f'\r{"-" * i} GCP-PermEnum {"-" * i} {message} {"-" * i}')
        sys.stdout.flush()
        time.sleep(delay)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Test IAM permissions for a Google Cloud project.")
    parser.add_argument("-p", "--projectid", required=True, help="Google Cloud Project ID")
    parser.add_argument("-k", "--keyfile", required=True, help="Path to the service account key file (JSON)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    PROJECT_ID = args.projectid
    KEY_FILE_PATH = args.keyfile

    if not os.path.exists(KEY_FILE_PATH):
        sys.exit(f"Error: Key file not found at {KEY_FILE_PATH}")

    print_banner()
    print_animated_message("Starting...", delay=0.2)

    print("\n" + "\n" + "=" * 80)
    print(f'Google Cloud Project ID: {PROJECT_ID}')
    print(f'Service Account Key File: {KEY_FILE_PATH}')
    print("=" * 80)

    # Create credentials using service account key file
    credentials = google.oauth2.service_account.Credentials.from_service_account_file(KEY_FILE_PATH)

    
    # Redirect errors to a file
    error_log_path = "error_log.txt"
    sys.stderr = open(error_log_path, "w")
    

    # Split testable permissions list into lists of 100 items each
    chunked_permissions = (
        [permissions[i * 100:(i + 1) * 100] for i in range((len(permissions)+99) // 100)])

    # Build cloudresourcemanager REST API python object
    crm_api = discovery.build('cloudresourcemanager',
                              'v1', credentials=credentials)

    given_permissions = []
    # For each list of 100 permissions, query the API to see if the service account has any of the permissions
    for permissions_chunk in chunked_permissions:
        try:
            response = crm_api.projects().testIamPermissions(resource=PROJECT_ID, body={
                'permissions': permissions_chunk}).execute()
            # If the service account has any of the permissions, add them to the output list
            if 'permissions' in response:
                given_permissions.extend(response['permissions'])
        except HttpError as e:
            print_animated_message(f"...")
            # Continue to the next iteration even if there's an error

    # Reset stderr to the default
    sys.stderr = sys.__stderr__

    print("\n" + "=" * 80)
    print("Allowed Permissions:", given_permissions)
    print("=" * 80)
    print(f"Errors (if any) are logged in {error_log_path}")
