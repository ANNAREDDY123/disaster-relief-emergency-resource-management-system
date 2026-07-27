VALID_CAMP_STATUS = [
    "Active",
    "Full",
    "Closed"
]


def valid_camp_status(status: str):

    return status in VALID_CAMP_STATUS


def has_available_capacity(camp):

    return camp.available_capacity > 0


def update_capacity_on_registration(camp):

    camp.available_capacity -= 1

    if camp.available_capacity <= 0:

        camp.available_capacity = 0

        camp.status = "Full"


def update_capacity_on_discharge(camp):

    camp.available_capacity += 1

    if camp.available_capacity > camp.capacity:

        camp.available_capacity = camp.capacity

    if camp.status != "Closed":

        camp.status = "Active"


def valid_resource_quantity(quantity: int):

    return quantity > 0


def sufficient_stock(available_stock: int, requested_quantity: int):

    return available_stock >= requested_quantity


def volunteer_can_be_assigned(volunteer):

    return volunteer.assigned_camp is None


def duplicate_email_exists(user):

    return user is not None
