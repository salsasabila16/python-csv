def validate_amount(amount):
    if amount <= 0:
        return False

    return True


def validate_transfer(sender, receiver):
    if sender.account_number == receiver.account_number:
        return False

    return True


