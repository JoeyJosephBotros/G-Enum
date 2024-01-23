---

# G-Enum 🚀

                        ('-.       .-') _             _   .-')    
                      _(  OO)     ( OO ) )           ( '.( OO )_  
  ,----.             (,------.,--./ ,--,' ,--. ,--.   ,--.   ,--.)
 '  .-./-')    .-')   |  .---'|   \ |  |\ |  | |  |   |   `.'   | 
 |  |_( O- ) _(  OO)  |  |    |    \|  | )|  | | .-') |         | 
 |  | .--, \(,------.(|  '--. |  .     |/ |  |_|( OO )|  |'.'|  | 
(|  | '. (_/ '------' |  .--' |  |\    |  |  | | `-' /|  |   |  | 
 |  '--'  |           |  `---.|  | \   | ('  '-'(_.-' |  |   |  | 
  `------'            `------'`--'  `--'   `-----'    `--'   `--' 

G-Enum is a powerful tool designed to enumerate the permissions of Google Cloud Platform (GCP) service accounts. It provides an efficient way to test IAM permissions for a specified Google Cloud project.

## Features

✨ **Efficient Enumeration**: G-Enum efficiently tests IAM permissions in chunks, providing a smooth and effective enumeration process.

🌐 **GCP Project Support**: Specify your Google Cloud Project ID using the `-p` or `--projectid` flag.

🔑 **Service Account Key File**: Use the `-k` or `--keyfile` flag to provide the path to your service account key file (JSON).

🚀 **Animated Interface**: Enjoy a dynamic and animated interface that enhances the user experience during the enumeration process.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/g-enum.git
   ```

2. Navigate to the project directory:
   ```bash
   cd g-enum
   ```

3. Install dependencies (ensure you have Python installed):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python g_enum.py -p <Your_Project_ID> -k <Path_to_Service_Account_Key_File.json>
```

## Example

```bash
python g_enum.py -p my-gcp-project -k /path/to/keyfile.json
```

## Known Issues

- Some permissions may not be valid for certain resources. Refer to the GCP documentation for more details.

## Support and Contribution

👩‍💻 Contributions and bug reports are welcome! Feel free to open an issue or submit a pull request.

📧 For support and inquiries, contact Joey Joseph at [joey.a.joseph@gmail.com].


Feel free to replace placeholder values with your actual information and customize the sections as needed.
