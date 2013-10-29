## Fitbit Exporter

This helps you export your Fitbit data into a nice JSON file.

## Usage

* First get your user token and secret.

        ./fitbit/gather_keys_cli.py

* Then place it appropriately in [export.py](export.py) as `user_key` and `user_secret` respectively.

* Then run the exporter.

        ./fitbit/export.py > export.json

## License

MIT.
