# Couchbase Parallel Data Inserter

This Python script allows you to insert randomly generated dummy data into a Couchbase bucket using parallel threads. It can be configured using command-line arguments, making it flexible for different use cases.

- Inserts dummy data into a Couchbase bucket.
- Supports parallel data insertion using multiple threads.
- Command-line interface for easy configuration.
- Configurable for the number of records and threads.

### Configuration via CLI

You can configure the script through the command line using the following options:

- `--host`: **(Required)** Couchbase host (e.g., `localhost:8091`)
- `--username`: **(Required)** Couchbase username
- `--password`: **(Required)** Couchbase password
- `--bucket`: **(Required)** Couchbase bucket name
- `--records`: **(Optional)** Number of records to insert, default is `10000`
- `--threads`: **(Optional)** Number of parallel threads to use, default is `1`

### Example Usage

./cb_loader.py --host localhost --username myuser --password mypass --bucket mybucket --records 50000 --threads 5

Note: If you need different data for specific test scenarios. You can edit the data_generatory.py file according to the way you keep the data and insert it.
