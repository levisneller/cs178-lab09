# code to read Books database from DynamoDB

import boto3

REGION = "us-east-1"
TABLE_NAME = "Books"


def get_table():
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_book(book):
    title = book.get("Title", "Unknown Title")
    author = book.get("Author", "Unknown Author")
    year = book.get("Year", "Unknown Year")

    print(f"  Title  : {title}")
    print(f"  Author : {author}")
    print(f"  Year   : {year}")
    print()


def print_all_books():
    table = get_table()
    
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No books found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} book(s):\n")
    for book in items:
        print_book(book)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_books()


if __name__ == "__main__":
    main()