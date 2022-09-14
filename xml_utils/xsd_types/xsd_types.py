"""XSD types utils
"""


def get_xsd_types(namespace_prefix=""):
    """Returns the list of all supported XSD types

    Args:
        namespace_prefix:

    Returns:

    """
    if namespace_prefix != "":
        namespace_prefix += ":"
    return [
        f"{namespace_prefix}anyType",
        f"{namespace_prefix}string",
        f"{namespace_prefix}normalizedString",
        f"{namespace_prefix}token",
        f"{namespace_prefix}duration",
        f"{namespace_prefix}dateTime",
        f"{namespace_prefix}time",
        f"{namespace_prefix}date",
        f"{namespace_prefix}gYearMonth",
        f"{namespace_prefix}gYear",
        f"{namespace_prefix}gMonthDay",
        f"{namespace_prefix}gDay",
        f"{namespace_prefix}gMonth",
        f"{namespace_prefix}boolean",
        f"{namespace_prefix}base64Binary",
        f"{namespace_prefix}hexBinary",
        f"{namespace_prefix}float",
        f"{namespace_prefix}double",
        f"{namespace_prefix}anyURI",
        f"{namespace_prefix}QName",
        f"{namespace_prefix}decimal",
        f"{namespace_prefix}integer",
        f"{namespace_prefix}nonPositiveInteger",
        f"{namespace_prefix}negativeInteger",
        f"{namespace_prefix}long",
        f"{namespace_prefix}nonNegativeInteger",
        f"{namespace_prefix}unsignedLong",
        f"{namespace_prefix}positiveInteger",
        f"{namespace_prefix}unsignedInt",
        f"{namespace_prefix}unsignedShort",
        f"{namespace_prefix}unsignedByte",
        f"{namespace_prefix}long",
        f"{namespace_prefix}int",
        f"{namespace_prefix}short",
        f"{namespace_prefix}byte",
    ]


def get_xsd_numbers(namespace_prefix=""):
    """Returns a list of formatted xsd number types

    Args:
        namespace_prefix:

    Returns:

    """
    if namespace_prefix != "":
        namespace_prefix += ":"
    return [
        f"{namespace_prefix}byte",
        f"{namespace_prefix}int",
        f"{namespace_prefix}integer",
        f"{namespace_prefix}long",
        f"{namespace_prefix}negativeInteger",
        f"{namespace_prefix}nonNegativeInteger",
        f"{namespace_prefix}nonPositiveInteger",
        f"{namespace_prefix}positiveInteger",
        f"{namespace_prefix}short",
        f"{namespace_prefix}unsignedLong",
        f"{namespace_prefix}unsignedInt",
        f"{namespace_prefix}unsignedShort",
        f"{namespace_prefix}unsignedByte",
        f"{namespace_prefix}float",
        f"{namespace_prefix}double",
        f"{namespace_prefix}decimal",
    ]


def get_xsd_floating_numbers(namespace_prefix=""):
    """Returns a list of formatted xsd floating number types

    Args:
        namespace_prefix:

    Returns:

    """
    if namespace_prefix != "":
        namespace_prefix += ":"
    return [
        f"{namespace_prefix}float",
        f"{namespace_prefix}double",
        f"{namespace_prefix}decimal",
    ]


def get_xsd_gregorian_types(namespace_prefix=""):
    """Returns a list of formatted xsd Gregorian date types

    Args:
        namespace_prefix:

    Returns:

    """
    if namespace_prefix != "":
        namespace_prefix += ":"
    return [
        f"{namespace_prefix}gYearMonth",
        f"{namespace_prefix}gYear",
        f"{namespace_prefix}gMonthDay",
        f"{namespace_prefix}gDay",
        f"{namespace_prefix}gMonth",
    ]
