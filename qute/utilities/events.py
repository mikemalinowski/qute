from ..vendor import Qt


# ------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
def printEventName(event):
    """
    Prints the name of the event type being given.

    :param event: The event to print the type of
    :type event: QEvent

    :return: None
    """
    event_type = event.type()
    for attr in dir(Qt.QEvent):
        if event_type == getattr(Qt.QEvent, attr):
            print(attr)
