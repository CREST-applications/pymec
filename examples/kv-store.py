from pymec import PleiadesClient
import logging


# SERVER_URL = "http://192.168.168.127:8332/api/v0.5"
SERVER_URL = "https://mecrm.dolylab.cc/api/v0.5-snapshot"


def main():
    logger = get_logger()

    # Create a client
    client = PleiadesClient(SERVER_URL, logger=logger)

    # New namespace instance in local
    namespace = client.new_kv_namespace()

    # Create a namespace in remote
    namespace.create()
    # or you can select existing namespace
    # namespace.set_namespace_id("<namespace_id>")

    # New key handler
    handler = namespace.new_key("pymec-example-key")

    # Set value
    handler.set("Hello, World!")

    # Get value
    for _ in range(3):
        print(handler.get())


def get_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    # handler.setFormatter(
    #     logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # )
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger


if __name__ == "__main__":
    main()
