import os
import uuid


def get_file_name(instance, filename):
    """
    function to create unique names for images
    :param instance:
    :param filename:
    :return:
    """
    ext = filename.strip().split('.')[-1]
    new_file_name = f'{uuid.uuid4()}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), new_file_name)
