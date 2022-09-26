""" Client library for Xerces validator.
"""
import logging

logger = logging.getLogger(__name__)


def send_message(
    message,
    endpoint="tcp://127.0.0.1:5555",
    timeout=3000,
    retries=3,
    context_zmq=7,
):
    """Send a message to the Schema validation server

    Args:
        message: JSON structure containing parameters
        endpoint:
        timeout:
        retries:
        context_zmq:

    Returns:

    """
    try:
        import zmq

        context = zmq.Context(context_zmq)

        logger.debug("Connecting to server...")
        socket = context.socket(zmq.REQ)
        socket.connect(endpoint)

        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)

        retries_left = retries
        request = 0
        reply = ""

        while retries_left:
            request += 1

            logger.info("Sending request %s...", request)
            socket.send(message)

            expect_reply = True
            while expect_reply:
                socks = dict(poll.poll(timeout))
                if socks.get(socket) == zmq.POLLIN:
                    reply = socket.recv()
                    if not reply:
                        break
                    else:
                        logger.info("Answer: %s", reply)
                        if reply == "ok":
                            reply = None
                        retries_left = 0
                        expect_reply = False
                else:
                    logger.warning("No response from server, retrying...")
                    # Socket is confused. Close and remove it.
                    socket.setsockopt(zmq.LINGER, 0)
                    socket.close()
                    poll.unregister(socket)
                    retries_left -= 1
                    if retries_left == 0:
                        reply = (
                            "Error: XML Validation server seems to be offline, please contact "
                            "the administrator."
                        )
                        break

                    logger.info("Reconnecting and resending...")
                    # Create new connection
                    socket = context.socket(zmq.REQ)
                    socket.connect(endpoint)
                    poll.register(socket, zmq.POLLIN)
                    socket.send(message)

        socket.close()
        context.term()

        if reply == "ok":
            return None
        return reply
    except ImportError:
        logger.error("pyzmq is not installed.")
