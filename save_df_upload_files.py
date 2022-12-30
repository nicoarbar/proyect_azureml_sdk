
# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, 'azure_sdk_blob01')
az_dataset        = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store  = ws.get_default_datastore()


# -----------------------------------------------------
# Load the Azureml Dataset into the pandas dataframe
# -----------------------------------------------------
df = az_dataset.to_pandas_dataframe()
# we can now work with the pandas data locally without reading csv from a local path


# -----------------------------------------------------
# Upload the dataframe to the azureml dataset
# -----------------------------------------------------
df_sub = df[["Married", "Gender", "Loan_Status"]]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
                dataframe=df_sub,
                target=az_store,
                name="Loan Dataset From Dataframe")



# Upload local files to storage account using datastore 
# -----------------------------------------------------
files_list = ["./data/test.csv", "./data/test1.csv"]

az_store.upload_files(files=files_list,
                      target_path="Loan Data/",
                      relative_root="./data/",
                      overwrite=True)


# -----------------------------------------------------
# Upload folder or directory to the storage account
# -----------------------------------------------------
az_store.upload(src_dir="./data",
                target_path="Loan Data/data",
                overwrite=True)












