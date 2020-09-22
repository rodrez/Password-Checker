# Author: Fabian Rodriguez
# Date: 09/02/2020
# Objective: Use pwned API to verify if a password has been leaked.

# Importlib use to handle import errors in a more pythonic approach
from importlib import import_module
libraries = ['requests', 'hashlib', 'sys', 'colorama', 'os', 'random', 'string']

for libname in libraries:
    try: 
        lib =   import_module(libname)
    except ImportError:
        print(f'There was an issue importing {libname}')
    else:
        globals()[libname] = lib


#
def request_api_data(query_char):
    """
    Summary
    -------
    Request the data from the pwned API

    Parameters
    ----------
    query_char : [str]
        Instead of using the whole sha1 key, the api uses k anonymity (5 first characters of the sha1) to maintain our password secure

    Returns
    -------
    [str]
        Response of pwned api given the correct query_char(5 first characters of your sha1 hashed password

    Raises
    ------
    RuntimeError
        Ensures the API status code is the correct one.
    """

    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    
    # 
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching, status {res.status_code}. Ensure API is using K anonymity and try again.")
    
    return res


def read_password_file(filenames):
    """
    Summary
    -------
    Read the lines of the file and use the words for password verification. 

    Parameters
    ----------
    filenames : [txt]
        Any .txt file containing a word per line

    Returns
    -------
    [list]
        A list of the words stored in the tex files
    """
    for file in filenames:
        with open(file, 'r') as f:
            passwords = f.readlines()

        return passwords

def get_password_leaks_count(hashes, hash_to_check):
    """
    Summary
    -------
    Compares the hashes to the hash_to_check and counts how many time has the password was leaked.

    Parameters
    ----------
    hashes : [str]
        hashes to compare against. Either your own leaked hashes or hashes from the pwned api response.
    hash_to_check : [str]
        hash to be verified

    Returns
    -------
    [int]
        The total count of how many times has the password been link, if any.
    """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_check(password):

    """
    Summary
    -------
    Checks if a password has been leaked using the pwned API. There is a combination of sha1, K anonymity
        and encoding to ensure password security.

    Parameters
    ----------
    password : [str, int]
        Password to be verified.

    Returns
    -------
    [tuple]
        A response and the tail of the password converted to sha1 to be used 
    """

    
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, tail = sha1_password[:5],sha1_password[5:] 

    response = request_api_data(first_5)
    
    return get_password_leaks_count(response, tail) 


def pass_gen(length, security):
    
    bad_chars = ['`', "'", '"']
    special_chars = [char for char in string.punctuation if char not in bad_chars]
    lower_letters = [letter for letter in string.ascii_lowercase]
    upper_letters = [letter for letter in string.ascii_uppercase]
    numbers = [str(num) for num in range(10)]

    password = ""
    pswd = []
    chars = [special_chars, lower_letters, upper_letters, numbers]

    if security == "max":
        for _ in range(length):
            if len(password) == 0:
                password += random.choice(special_chars)
                password += random.choice(upper_letters)
                password += random.choice(lower_letters)
                password += random.choice(numbers)
            else:

                rand_selection = random.choice(chars)
                rand_chars = rand_selection[random.randrange(len(rand_selection))]
                
                password += rand_chars

            if len(password) >= length:
                break
        pswd.append(password) 
    return pswd


def main(args):
    
    for password in args:
        count = pwned_check(password.strip())
        if count:
            print(f"The password {password.strip()} was found {count} times 😰. You might want to change it.")
        else:
            print(f"Great news! {password.strip()} was not found. 😎")
    return "Password verification completed. ✅"

if __name__ == '__main__':

    # print(colorama.Fore.RED + "Hello! Although the program works inputing the password as an command line argument,\nit is highly encourage to use a txt file for security purposes." + colorama.Style.RESET_ALL)
    # # Loops through the arguments passed and decides if the file exists
    # for args in sys.argv[1:]:
    #     if os.path.exists(args):
    #         sys.exit(main(read_password_file(sys.argv[1:])))
    #     else:
    #         sys.exit(main(sys.argv[1:]))

    main(pass_gen(4, "max"))