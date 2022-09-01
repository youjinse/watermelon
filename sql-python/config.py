import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://watermelondb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'AfTwTdEF4HP3Kox7qlHirA0BKJo7CWNY5DryEjBnzC2JO9G9jqm95kFyeADH6io2wpCKY4BfMJexFKdtjlID0A=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}