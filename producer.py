"""
    This program sends a message to a queue on the RabbitMQ server.

"""
# Import from Python Standard Library

import sys
import os
import csv
import time
import logging
import pika

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Declare program constants (typically constants are named with ALL_CAPS)

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "netflix_titles.csv"
OUTPUT_FILE_NAME = "emitted_message.csv"


# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="netflix_queue")


# Define program functions (bits of reusable code)


def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""

    (
        show_id,
        type,
        title,
        director,
        cast,
        country,
        date_added,
        release_year,
        rating,
        duration,
        listed_in,
        description,
    ) = row

    # use an fstring to create a message from our data
    fstring_message = f"[{type}, Title: {title}, Release: {release_year}, Will be Added: {date_added}]"

    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared message: {fstring_message}")
    return MESSAGE


def stream_row(input_file_name, address_tuple):
    """Read from input file and stream data."""
    logging.info(f"Starting to stream data from {input_file_name} to {address_tuple}.")

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")
        rows = list(reader)

        last_processed_index = 0  # Track the index

    with open(OUTPUT_FILE_NAME, "w") as output_file:
        logging.info(f"Opened for writing: {OUTPUT_FILE_NAME}.")
        while True:
            for i in range(last_processed_index, len(rows)):
                row = rows[i]
                MESSAGE = prepare_message_from_row(row)
                output_file.write(str(MESSAGE) + "\n")
                # use the channel to publish a message to the queue
                ch.basic_publish(exchange="", routing_key="netflix_queue", body=MESSAGE)
                logging.info(f"Sent and wrote: {MESSAGE} on port {PORT}.")
                last_processed_index = len(rows)  # Update the index
                time.sleep(3)


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, ADDRESS_TUPLE)
        logging.info("Streaming complete!")
        logging.info("===============================================")
        
        # print a message to the console for the user
        print(" [x] Sent 'Hello Netflix!'")
        # close the connection to the server
        conn.close()

    except Exception as e:
        logging.error(f"An error occurred: {e}")





