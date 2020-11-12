import os


_RESOURCE_DIR = os.path.join(
    os.path.dirname(__file__),
    '_res',
)


# ------------------------------------------------------------------------------
def get(name):
    return os.path.join(
        _RESOURCE_DIR,
        name,
    ).replace('\\', '/')


# ------------------------------------------------------------------------------
def all():
    files = list()
    for filename in os.listdir(_RESOURCE_DIR):
        files.append(os.path.join(_RESOURCE_DIR, filename).replace('\\', '/'))
    return files
