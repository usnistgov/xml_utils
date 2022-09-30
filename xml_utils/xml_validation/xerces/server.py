""" Server code for Xerces validator.
"""
import argparse
import json
import logging
import sys
import time

logger = logging.getLogger(__name__)


def _xerces_exists():
    """Check if xerces wrapper is installed

    Returns:

    """
    try:
        __import__("xerces_wrapper")
    except ImportError:
        logger.error("XERCES DOES NOT EXIST")
        return False
    else:
        logger.debug("XERCES EXISTS")
        return True


def _xerces_validate_xsd(xsd_string):
    """Validate schema using Xerces

    Args:
        xsd_string:

    Returns:
        errors

    """
    if not _xerces_exists():
        return "Xerces is not installed"

    import xerces_wrapper

    logger.debug("XERCES IMPORTED")
    error = xerces_wrapper.validate_xsd(xsd_string)
    logger.debug("SCHEMA validated")
    if len(error) <= 1:
        logger.debug("SCHEMA valid")
        error = None

    return error


def _xerces_validate_xml(xsd_string, xml_string):
    """Validate document using Xerces

    Args:
        xsd_string:
        xml_string:

    Returns:
        errors

    """
    if not _xerces_exists():
        return "Xerces is not installed"

    import xerces_wrapper

    logger.debug("XERCES IMPORTED")
    error = xerces_wrapper.validate_xml(xsd_string, xml_string)
    logger.debug("DATA validated")
    if len(error) <= 1:
        logger.debug("DATA valid")
        error = None

    return error


def main(argv):
    """main"""

    parser = argparse.ArgumentParser(description="Launch Server Tool")

    # add optional arguments
    parser.add_argument(
        "-e", "--endpoint", help="Listening endpoint", nargs=1, required=True
    )

    parser.add_argument(
        "-c", "--contextzmq", help="Context zmq", nargs=1, required=True
    )

    # parse arguments
    args = parser.parse_args()

    # get optional arguments
    if args.endpoint:
        endpoint = args.endpoint[0]
    else:
        endpoint = "tcp://127.0.0.1:5555"

    if args.contextzmq:
        context_zmq = int(args.contextzmq[0])
    else:
        context_zmq = 7

    # socket configuration
    try:
        import zmq

        context = zmq.Context(context_zmq)
        socket = context.socket(zmq.REP)
        socket.bind(endpoint)

        mutex = True
        while True:
            if mutex:
                #  Wait for next request from client
                message = socket.recv()
                logger.debug("Received request")

                try:
                    message = json.loads(message)

                    # validate data against schema
                    if "xml_string" in message:
                        logger.debug("VALIDATE XML")
                        mutex = False
                        try:
                            xsd_string = message["xsd_string"].encode("utf-8")
                        except UnicodeEncodeError:
                            xsd_string = message["xsd_string"]

                        try:
                            xml_string = message["xml_string"].encode("utf-8")
                        except UnicodeEncodeError:
                            xml_string = message["xml_string"]

                        error = _xerces_validate_xml(xsd_string, xml_string)

                        if error is None:
                            error = "ok"

                        response = error
                    else:
                        logger.debug("VALIDATE XSD")
                        mutex = False
                        try:
                            xsd_string = message["xsd_string"].encode("utf-8")
                        except UnicodeEncodeError:
                            xsd_string = message["xsd_string"]

                        error = _xerces_validate_xsd(xsd_string)

                        if error is None:
                            error = "ok"

                        response = error

                    logger.debug(response)

                    socket.send(str(response))
                    mutex = True
                    logger.debug("Sent response")
                except Exception as exception:
                    logger.error(str(exception))

            time.sleep(1)
    except ImportError:
        logger.error("pyzmq is not installed.")


if __name__ == "__main__":
    main(sys.argv[1:])
