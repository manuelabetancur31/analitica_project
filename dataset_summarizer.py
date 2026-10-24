import io
import pandas as pd


class DatasetSummarizer:
    """Clase encargada de recibir un DataFrame de Pandas y generar

    un reporte estructurado en formato de texto (.txt).
    """

    def __init__(
        self, dataframe: pd.DataFrame, output_path: str = "resumen_dataset.txt"
    ):
        self.df = dataframe
        self.output_path = output_path

    def generate_summary(self) -> str:
        if self.df is None or self.df.empty:
            raise ValueError("El DataFrame está vacío o no ha sido proporcionado.")

        buffer = io.StringIO()
        self.df.info(buf=buffer)
        info_str = buffer.getvalue()

        resumen = []
        resumen.append("=" * 60)
        resumen.append("          RESUMEN EJECUTIVO DEL DATAFRAME")
        resumen.append("=" * 60 + "\n")

        resumen.append("1. DIMENSIONES GENERALES:")
        resumen.append(f"   - Cantidad de Filas: {self.df.shape[0]}")
        resumen.append(f"   - Cantidad de Columnas: {self.df.shape[1]}\n")

        resumen.append("2. ESTRUCTURA Y TIPOS DE DATOS (df.info()):")
        resumen.append(info_str + "\n")

        resumen.append("3. PRESENCIA DE VALORES NULOS:")
        nulls = self.df.isnull().sum()
        for col, count in nulls.items():
            resumen.append(f"   - {col}: {count} nulos")
        resumen.append("\n")

        resumen.append("4. ESTADÍSTICAS DESCRIPTIVAS (df.describe()):")
        resumen.append(self.df.describe(include="all").to_string())
        resumen.append("\n" + "=" * 60)

        summary_text = "\n".join(resumen)

        with open(self.output_path, "w", encoding="utf-8") as file:
            file.write(summary_text)

        print(f"Resumen generado exitosamente en: '{self.output_path}'")
        return summary_text