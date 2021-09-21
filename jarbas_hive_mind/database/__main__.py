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
            print("{:<8} {:<15} {:<16}".format('id:','name:','api key:'))
            for x in db.get_clients():
                if x["client_id"] > 0:
                    print("{:<8} {:<15} {:<16}".format(x["client_id"], str(x["name"]), str(x["api_key"])))
    if args.action == 'delete':
        with ClientDatabase() as db:
            client_valid = False
            for x in db.get_clients_by_name(args.name):
                if x["api_key"] == args.access_key:
                    client_valid = True
            if client_valid == True:
                db.delete_client(args.access_key)
                print("API key was revoked")
            else:
                print("No client with this name or API key found")


if __name__ == '__main__':
    main()
