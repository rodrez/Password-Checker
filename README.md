# Password-Checker
- Check if password exists in API response
- First we use hashlib.sha1 to convert our password to sha1
- Inside the sha1 function we encode the password to utf-8, because Unicode objects must be encoded before hashing
- We use hexdigest to get the hexadecimal characters of our sha1 passwaord
- Since we need our K anonimity to be upper cased we also use the upper() function
- The API provides a list of all the passwords that have been leaked.
- The we compare our hashed password with the ones we got from the API.
- If our hash matches any of the hashes from the API we count how many leaks our password has been comproised.

# How to run
- git clone this repo
- pip install requirements.txt
- python3 check_my_pass.py passwords.txt

# Issues
- No issues so far
- Feel free to let me know if you find any issues.
