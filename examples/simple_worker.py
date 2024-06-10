from pymec import PleiadesClient


# SERVER_URL = "http://192.168.168.127:8332/api/v0.5"
SERVER_URL = "http://172.21.39.32:8332/api/v0.5"
# SERVER_URL = "https://mecrm.dolylab.cc/api/v0.5-snapshot"


def main():
    # Create a client
    client = PleiadesClient(SERVER_URL)

    # Create a worker
    worker = (
        client.new_worker()
        .set_runtimes(
            [
                "pymec+hello",
            ]
        )
        .register()
        .set_tags(["python3.10"])
    )

    # Wait for a job
    job = worker.wait_contract()
    # _ = job.lambda_.blob.data

    # Process the data
    input_data = job.get_input().get_data().decode("utf-8")
    output_data = f"{input_data}, MEC-RM!".encode("utf-8")

    # create output blob
    output_blob = client.new_blob().from_bytes(output_data)

    # Finish the job and send the output data to the requester
    job.finish(output_blob)


if __name__ == "__main__":
    main()
