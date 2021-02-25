import re
import sys


def validate_phone_number(arm_phone_num):
    """
    Gets a phone number and returns True if the format of the number is Armenian
    and False otherwise

    Parameters
    __________
    arm_phone_num : str
        the phone number as a string

    Returns
    _______
    bool
        True, if the number it got IS a valid Armenian phone number format
        False, if the number it got IS NOT a valid Armenia phone number format
    """

    """
    only 55, 77, 91, 98, 99 operator-codes are given in the homework
    we assume that 00-00-00 is a valid phone number
    """

    rules = (
            '0?'  # there might or might not be a zero before the operator-code
            '(55|77|91|98|99)'  # operator-codes
            '[ -]?'  # there might or might not be either a space or a dash between the operator-code and the number
            '('
                    r'\d{6}'  # either a number without any spaces or dashes
                '|'
                    r'\d{3}[ -]\d{3}'  # or a number in '123-456' or '123 456' format
                '|'
                    r'\d{2} \d{2} \d{2}'  # or a number in '12 34 56' format
                '|'
                    r'\d{2}-\d{2}-\d{2}'  # or a number in '12-34-56' format
            ')'
    )  # notice that '12-34 56' and '12 34-56' formats are not going to be valid

    return re.fullmatch(rules, arm_phone_num)


def validate_email(address):
    """
    Gets an email address and returns True if it's a valid email format
    and False otherwise

    Parameters
    __________
    address : str
        the email address as a string

    Returns
    _______
    bool
        True, if the address IS in a valid email format
        False, if the address IS NOT in a valid email format
    """

    """
    looked up literature:
    https://docs.python.org/3/library/re.html
    https://en.wikipedia.org/wiki/Email_address#Syntax
    https://en.wikipedia.org/wiki/Hostname#Syntax
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s09.html

    This homework exercise is limited to only one regular expression thus
    ONLY SOME OF THE EMAIL VARIATIONS ARE VALIDATED BY THIS EMAIL VALIDATOR
    """

    rules = (
        # the email address is a 'local-part@domain' construction
        # domain is a 'HOSTNAME_LABEL.top_level_domain' construction e.g. 'gmail.com'
        '('
            r'(?=.{1,64}@.{1,255}$)'  # limiting local-part to 64 and domain to 255 characters
            r'^[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # local-part without quotes can include ANYTHING BUT THESE CHARACTERS
                                             # these characters are only allowed inside a quoted local-part (see below)
            '('
                r'\.?'                           # same pattern can continue after a dot, two or more consecutive
                r'[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # dots are not allowed, at lease one other character after the dot
            ')*'                                # for 0 or more times
        '|'
            r'(?=.{1,66}@.{1,255}$)'  # limiting local-part to 64 (excluding quotes) and domain to 255 characters
            r'\"'
                r'[^\\"]*'  # local-part can be anything if written between quotes, except '\' and '"'
            r'\"'           # for the sake of this homework I have simplified the rules for a quoted local-part
        ')'                # for more info about limitations of the local-part in quotes go to wikipedia mentioned above
    '@'
        r'[a-zA-Z\d]+'           # HOSTNAME_LABEL is a combination of alphanumerics and the hyphen
        '('
            r'[\-a-zA-Z\d]*'             # except it CAN'T START OR END with a hyphen
            r'[a-zA-Z\d]+'               # at least one alphanumeric character after hyphen
        ')*'                    # for 0 or more times
        '('
            r'\.'                    # the HOSTNAME_LABEL pattern repeated after a dot, two or more consecutive
            r'[a-zA-Z\d]+'           # dots are not allowed, at least one other character after the dot
            '('
                r'[\-a-zA-Z\d]*'
                r'[a-zA-Z\d]+'           # at least one alphanumeric character after hyphen
            ')*'                    # for 0 or more times
        ')*'                    # for 0 or more times
    r'\.'
        r'([a-zA-Z]{2,})'  # top_level_domain names (e.g. .com .org .net) are two or more characters long
                          # the 'co' in '.co.uk' is handled in the code-lines between '@' and r'\.' right above
    )

    # the maximum of 63 character limitation of each HOSTNAME_LABEL is not validated with this regex
    # but overall 255 character domain limitation IS validated

    return re.fullmatch(rules, address)


def validate_broker(command, value=None, *, check_if_command_exists=False):
    """
    Gets a value and a format type and prints whether
    the value is a valid instance of that format type.
    Also can check whether a format type (command) exists.


    Parameters
    __________
    command : str
        the format type to validate the value against
    value : str, optional
        the value to be validated
    check_if_command_exists : bool, optional
        used when checking whether the command exists

    Returns
    _______
    None
        This function only prints when check_if_command_exists = False
    bool
        True, if given command exists
        False, if given command DOES NOT exist
        this works only if check_if_command_exists = True
    """

    validators_list = ('email', 'phone_number')
    format_dict = {'email': 'email address', 'phone_number': 'Armenian phone number'}

    if check_if_command_exists:
        return command in validators_list

    if command == validators_list[0]:
        validated = validate_email(value)
        formatting = 'email address'
    elif command == validators_list[1]:
        validated = validate_phone_number(value)
        formatting = 'Armenian phone number'
    else:
        print('No such command.\n')
        return

    if validated:
        print(f'YES, this IS a valid {formatting} format\n')
    else:
        print(f'No, this IS NOT a valid {formatting} format\n')


if __name__ == '__main__':
    # Please make sure to type correct quote characters when using command line arguments

    no_exception_when_assigning_to_command = True

    try:
        command = sys.argv[1]
    except IndexError:
        no_exception_when_assigning_to_command = False
        command = input('Type one of the following commands.\n'
                        'email\n'
                        'phone_number\n')

    if validate_broker(command.lower(), check_if_command_exists=True):
        try:
            value = sys.argv[2]
        except IndexError:
            if no_exception_when_assigning_to_command:
                print('No value passed.')
            value = input('Please type the value without quotes.\n')

        validate_broker(command.lower(), value)
    else:
        print('No such command.\n')
