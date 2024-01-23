# G-Enum
G-Enum 🚀

G-Enum is a powerful tool designed to enumerate the permissions of Google Cloud Platform (GCP) service accounts. It provides an efficient way to test IAM permissions for a specified Google Cloud project.

Features
✨ Efficient Enumeration: G-Enum efficiently tests IAM permissions in chunks, providing a smooth and effective enumeration process.

🌐 GCP Project Support: Specify your Google Cloud Project ID using the -p or --projectid flag.

🔑 Service Account Key File: Use the -k or --keyfile flag to provide the path to your service account key file (JSON).

🚀 Animated Interface: Enjoy a dynamic and animated interface that enhances the user experience during the enumeration process.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/g-enum.git
Navigate to the project directory:

bash
Copy code
cd g-enum
Install dependencies (ensure you have Python installed):

bash
Copy code
pip install -r requirements.txt
Usage
bash
Copy code
python g_enum.py -p <Your_Project_ID> -k <Path_to_Service_Account_Key_File.json>
Example
bash
Copy code
python g_enum.py -p my-gcp-project -k /path/to/keyfile.json
Known Issues
Some permissions may not be valid for certain resources. Refer to the GCP documentation for more details.
Support and Contribution
👩‍💻 Contributions and bug reports are welcome! Feel free to open an issue or submit a pull request.

📧 For support and inquiries, contact Joey Joseph at [email@example.com].
