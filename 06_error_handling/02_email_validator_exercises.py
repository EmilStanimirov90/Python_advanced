class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LEN = 5
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]
while True:
    email = input()
    if email == 'End':
        break
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    domain = '.' + domain.split('.')[-1]

    if len(name) < EMAIL_MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")

    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
