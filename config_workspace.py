"""
Creating the resources to execute just once 
"""

from azureml.core import Workspace, Datastore, Dataset

config_path = "./config"

# It will also create teh Azure services by default created in workspace creation
# key vault, app insights, storage,
ws = Workspace.create(name='<Your Workspace Name>',
                      subscription_id='<Your Subscription ID>',
                      resource_group='<Resource group Name',
                      create_resource_group=True,   # True if it does not exist
                      location='<Nearest Azure region>')

# Write the config.json file to local directory
# This file is needed for creation of other resources inside of the workspace like datasets
ws.write_config(path=config_path)

# Create Datastore
# origin of the data will be in the blob container
# but can come from any other source inside Azure

# Can reinstate the workspace from the config file
ws = Workspace.from_config(path=config_path)

az_store = Datastore.register_azure_blob_container(
            workspace=ws,
            datastore_name="azure_sdk_blob01",
            account_name="azuremlstb01", # name of the storage account
            container_name="azuremlstb01blob",
            account_key="mQ6meDug7SdlFXu0/tBu7pKcNerxxYtO6X1V13M4sSohBAv2/i2KxdYe3ueiQXKrw+alPU1ou4NBuYBtuBVsig==")


# Create dataset
az_store = Datastore.get(ws, datastore_name="azure_sdk_blob01")

# Create the path of the csv file
csv_path = [(az_store, "Loan Data/Loan Approval Prediction.csv")]

# Create the dataset
loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

# Register the dataset
loan_dataset = loan_dataset.register(workspace=ws,
                                     name="Loan Applications Using SDK",
                                     create_new_version=True)


"""
Listing all the created resources from Azure ML
"""

# List all the workspaces within a subscription
ws_list = Workspace.list(subscription_id="77819c59-5764-4995-8596-d09cdc661078")
ws_list = list(ws_list)

# Access the default datastore from workspace
az_default_store = ws.get_default_datastore()

# List all the datastores
store_list = list(ws.datastores)

# Get the dataset by name from a workspace
az_dataset = Dataset.get_by_name(ws, "Loan Applications Using SDK")

# if you want to acces to the data of the dataset, use the methods of the class created


# -----------------------------------------------------
# List datasets from a workspace
# -----------------------------------------------------

ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)
