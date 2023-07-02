import datetime

class Functions:
    """
    This class holds all functions needed for the data master update.
    It might evolve to more functions, when needed.
    """

    def group(self, param):
        try:
            print(f"group called with parameter: {param}")
            # Add your group method logic here
        except Exception as e:
            print("Error in group method:", e)

    def read(self, param):
        try:
            print(f"read called with parameter: {param}")
            # Add your read method logic here
        except Exception as e:
            print("Error in read method:", e)

    # ... Define other methods ...


if __name__ == "__main__":
    workflow_dict = {
        'read': ('Query_fvv', 'fvv'),
        'date': 'Datum',
        'clean': ('Format Name', 'Format'),
        'group': ('Date', 'Format Name'),
        'sum': 'Spendings',
        'write': ('table_fvv', 'data_master_fvv')
    }

    functions = Functions()

    # Call methods dynamically based on the dictionary
    try:
        for method_name, param in workflow_dict.items():
            method = getattr(functions, method_name)
            method(param)
    except Exception as e:
        print("Oops, something went wrong:", e)
