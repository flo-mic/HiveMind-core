import argparse
from jarbas_hive_mind.database import ClientDatabase


def main():
    parser = argparse.ArgumentParser(description="Modify HiveMind's database")
    parser.add_argument(
        "action",
        help="database action",
        choices=['list', 'add', 'delete'])
    parser.add_argument("--name", help="human readable name")
    parser.add_argument("--access_key", help="access key")
    parser.add_argument("--crypto_key", help="payload encryption key")
    args = parser.parse_args()
    # Check if a user was defined
    if args.action == 'add':
        with ClientDatabase() as db:
            db.add_client(
                args.name, args.access_key, crypto_key=args.crypto_key)
    if args.action == 'list':
        with ClientDatabase() as db:
            for x in db.get_clients():
                print (x)
    if args.action == 'delete':
        with ClientDatabase() as db:
            db.delete_client(
                args.name, args.access_key)


if __name__ == '__main__':
    main()
