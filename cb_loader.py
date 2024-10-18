import argparse
import logging
from concurrent.futures import ThreadPoolExecutor
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException, DocumentExistsException
from data_generator import generate_random_data
import random

# Logging ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CouchbaseConnector:
    def __init__(self, host, username, password, bucket_name):
        try:
            self.cluster = Cluster(f"couchbase://{host}",
                                   ClusterOptions(PasswordAuthenticator(username, password)))
            self.collection = self.cluster.bucket(bucket_name).default_collection()
            logging.info("Successfully connected to Couchbase.")
        except CouchbaseException as e:
            logging.error(f"Failed to connect to Couchbase: {e}")
            raise

    def insert_document(self, data):
        document_id = f"doc_{random.randint(1000000, 9999999)}"
        try:
            self.collection.insert(document_id, data)
            ##logging.info(f"Document inserted with ID: {document_id}")
        except DocumentExistsException:
            logging.warning(f"Document with ID {document_id} already exists. Skipping insert.")
        except CouchbaseException as e:
            logging.error(f"Error inserting document {document_id}: {e}")

def insert_documents(connector, num_records):
    for _ in range(num_records):
        data = generate_random_data()
        connector.insert_document(data)

def main():
    parser = argparse.ArgumentParser(description="Insert documents into Couchbase using CLI")
    parser.add_argument('--host', required=True, help='Couchbase host (example localhost:8091)')
    parser.add_argument('--username', required=True, help='Username for Couchbase')
    parser.add_argument('--password', required=True, help='Password for Couchbase')
    parser.add_argument('--bucket', required=True, help='Bucket name in Couchbase')
    parser.add_argument('--records', type=int, default=10000, help='Number of records to insert, default is 10000')
    parser.add_argument('--threads', type=int, default=1, help='Number of parallel threads to use')
    
    args = parser.parse_args()

    # Giriş parametrelerini ekrana yazdır
    logging.info(f"Starting insertion with the following parameters: Host={args.host}, Username={args.username}, Password={'*' * len(args.password)}, Bucket={args.bucket}, Records to insert={args.records}, Number of threads={args.threads}")

    connector = CouchbaseConnector(args.host, args.username, args.password, args.bucket)
    records_per_thread = args.records // args.threads
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(insert_documents, connector, records_per_thread) for _ in range(args.threads)]
        for future in futures:
            future.result()  # Wait for all threads to complete

    logging.info(f"Total records added: {args.records}")

if __name__ == '__main__':
    main()
