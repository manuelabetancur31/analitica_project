import pandas as pd
from datasets import load_dataset


class HFDatasetLoader:
    """Clase encargada de descargar datasets desde Hugging Face

    y convertirlos a DataFrames de Pandas.
    """

    def __init__(self, dataset_name: str, split: str = "train"):
        self.dataset_name = dataset_name
        self.split = split
        self.dataframe = None

    def fetch_as_dataframe(self) -> pd.DataFrame:
        try:
            print(
                f"Cargando dataset '{self.dataset_name}' (split: '{self.split}')..."
            )
            hf_dataset = load_dataset(self.dataset_name, split=self.split)
            self.dataframe = pd.DataFrame(hf_dataset)
            print("¡Carga exitosa!")
            return self.dataframe
        except Exception as e:
            print(f"Error al cargar el dataset: {e}")
            raise e