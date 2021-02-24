import re
import sys


def validate_phone_number(arm_phone_num):
    """
    only 55, 77, 91, 98, 99 codes are given in the homework
    we assume that 00-00-00 number is a valid number
    """

    rules = (
            '0?(55|77|91|98|99)'  # 0 can or cannot be before the code
            '[ -]?'
            '('
                '\d{6}'  # either a number without any spaces or dashes
            '|'
                '\d{3}[ -]\d{3}'  # or a number in '123-456' or '123 456' form
            '|'
                '\d{2} \d{2} \d{2}'  # or a number in '12 34 56' form
            '|'
                '\d{2}-\d{2}-\d{2}'  # or a number in '12-34-56' form
            ')'
    )  # notice that '12-34 56' and '12 34-56' forms are not going to be valid

    return re.fullmatch(rules, arm_phone_num)


def validate_email(address):
    """
    looked up literature:
    https://docs.python.org/3/library/re.html
    https://en.wikipedia.org/wiki/Email_address#Syntax
    https://en.wikipedia.org/wiki/Hostname#Syntax
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s09.html
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch02s16.html
    https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
    https://help.xmatters.com/ondemand/trial/valid_email_format.htm

    This homework exercise is limited to only one regular expression thus
    ONLY SOME OF THE EMAIL VARIATIONS ARE VALIDATED BY THIS EMAIL VALIDATOR
    """

    rules = (
        # the email address is a 'local-part@domain' construction
        '('
            '(?=.{1,64}@.{1,255}$)'  # limiting local-part to 64 and domain to 255 characters
            '^[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # local-part without quotes can include anything but these characters
                                             # these characters are only allowed inside a quoted string
            '('
                '\.?'
                '[^\(\)\,\:\;\<\>\@\[\]\.\s]+'  # same pattern can continue after a single dot
            ')*'                                # for 0 or more times
        '|'
            '(?=.{1,66}@.{1,255}$)'  # limiting local-part to 64 (excluding quotes) and domain to 255 characters
            '\"'
                '[^\\"]*'  # local-part can be anything if written between quotes, except '\' and '"'
            '\"'           # for the sake of this homework I have simplified the rules for a quoted local-part
        ')'
    '@'
        '[a-zA-Z\d]+([\-a-zA-Z\d]*[a-zA-Z\d]+)*'  # the hostname label is a combination of alphanumerics and the hyphen
                                                  # except it CAN'T START OR END with a hyphen
        '(\.[a-zA-Z\d]+([\-a-zA-Z\d]*[a-zA-Z\d]+)*)*'  # above pattern repeated after a single dot for 0 or more times
    '\.'
        '([a-zA-Z]{2,})'  # top-level domain names (e.g. .com .org .net) are two or more characters long
                          # the 'co' in '.co.uk' is handled in the code-lines between '@' and '\.' right above
    )

    # the maximum of 63 character limitation of each hostname label is not validated with this regex
    # but overall 255 character domain limitation IS validated

    return re.fullmatch(rules, address)


def validate_broker(command, value):
    if command == 'email':
        if validate_email(value):
            print('Yes, this is a valid email address syntax\n')
        else:
            print('No, this is NOT a valid email address syntax\n')
    elif command == 'phone_number':
        if validate_phone_number(value):
            print('Yes, this is a valid phone number form\n')
        else:
            print('No, this is NOT a valid phone number form\n')
    else:
        print('No such command.\n')


if __name__ == '__main__':
    # Please make sure to type correct quotes when using command line arguments

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
