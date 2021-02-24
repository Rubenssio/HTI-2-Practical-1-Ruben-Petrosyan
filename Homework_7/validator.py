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
            '0?(55|77|91|98|99)'  # 0 can or cannot be before the operator-code
            '[ -]?'
            '('
                '\d{6}'  # either a number without any spaces or dashes
            '|'
                '\d{3}[ -]\d{3}'  # or a number in '123-456' or '123 456' format
            '|'
                '\d{2} \d{2} \d{2}'  # or a number in '12 34 56' format
            '|'
                '\d{2}-\d{2}-\d{2}'  # or a number in '12-34-56' format
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
            '(?=.{1,64}@.{1,255}$)'  # limiting local-part to 64 and domain to 255 characters
            '^[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # local-part without quotes can include ANYTHING BUT THESE CHARACTERS
                                             # these characters are only allowed inside a quoted local-part (see below)
            '('
                '\.?'                           # same pattern can continue after a dot, two or more consecutive
                '[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # dots are not allowed, at lease one other character after the dot
            ')*'                                # for 0 or more times
        '|'
            '(?=.{1,66}@.{1,255}$)'  # limiting local-part to 64 (excluding quotes) and domain to 255 characters
            '\"'
                '[^\\"]*'  # local-part can be anything if written between quotes, except '\' and '"'
            '\"'           # for the sake of this homework I have simplified the rules for a quoted local-part
        ')'                # for more info about limitations of the local-part in quotes go to wikipedia mentioned above
    '@'
        '[a-zA-Z\d]+'           # HOSTNAME_LABEL is a combination of alphanumerics and the hyphen
        '('
            '[\-a-zA-Z\d]*'             # except it CAN'T START OR END with a hyphen
            '[a-zA-Z\d]+'               # at least one alphanumeric character after hyphen
        ')*'                    # for 0 or more times
        '('
            '\.'                    # the HOSTNAME_LABEL pattern repeated after a dot, two or more consecutive
            '[a-zA-Z\d]+'           # dots are not allowed, at lease one other character after the dot
            '('
                '[\-a-zA-Z\d]*'
                '[a-zA-Z\d]+'           # at least one alphanumeric character after hyphen
            ')*'                    # for 0 or more times
        ')*'                    # for 0 or more times
    '\.'
        '([a-zA-Z]{2,})'  # top_level_domain names (e.g. .com .org .net) are two or more characters long
                          # the 'co' in '.co.uk' is handled in the code-lines between '@' and '\.' right above
    )

    # the maximum of 63 character limitation of each hostname label is not validated with this regex
    # but overall 255 character domain limitation IS validated

    return re.fullmatch(rules, address)


def validate_broker(command, value):
    """
    Gets a value and a format type and prints whether
    the value is a valid instance of that format type

    Parameters
    __________
    command : str
        the format type the validate the value against
    value : str
        the value to be validated

    Returns
    _______
    None
        This function only prints
    """

    if command == 'email':
        if validate_email(value):
            print('Yes, this is a valid email address format\n')
        else:
            print('No, this is NOT a valid email address format\n')
    elif command == 'phone_number':
        if validate_phone_number(value):
            print('Yes, this is a valid Armenian phone number format\n')
        else:
            print('No, this is NOT a valid Armenian phone number format\n')
    else:
        print('No such command.\n')


if __name__ == '__main__':
    # Please make sure to type correct quote characters when using command line arguments

    command_assignment_gave_exception = False

    try:
        command = sys.argv[1]
    except IndexError:
        command = input('Type one of the following commands.\nemail\nphone_number\n')
        command_assignment_gave_exception = True

    try:
        if command_assignment_gave_exception:
            value = input('Please type the value without quotes.\n')
        else:
            value = sys.argv[2]
        validate_broker(command, value.lower())
    except IndexError:
        print('No value passed.')
        value = input('Please type the value without quotes.\n')
        validate_broker(command, value.lower())
