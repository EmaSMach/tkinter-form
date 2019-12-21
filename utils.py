# helper functions


def is_viable_string(obj):
    """Validates if the given object is a string,
    and if it's a meaningful one"""
    if isinstance(obj, str):
        if len(obj) > 0 and not obj.isspace():
            return True
        else:
            return False
    else:
        return False
