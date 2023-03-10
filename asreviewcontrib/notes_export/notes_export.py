import os
import re
import shutil
from pathlib import Path

import numpy as np
from asreview import ASReviewData, ASReviewProject, open_state


def export_notes(
    asreview_filename,
    output_filename,
    only_with_notes=False,
    labeling_order=False,
):
    """Export notes with data from ASReview file
    Parameters
    ----------
    asreview_filename: str,
        File name of ASreview file with .asreview extension

    output_filename: str,
        File name of output file with .csv extension

    only_with_notes: bool,
        Flag if True exports only records with notes to dataset csv

    labeling_order: bool,
        Flag if True exports labeling order with notes to dataset csv

    Returns
    -------
    None

    csv file is generated in the current directory
    """
    project_path = Path("tmp_data_notes_export")
    try:
        shutil.rmtree(project_path)
    except:
        pass

    project_path.mkdir(parents=True, exist_ok=True)
    project = ASReviewProject.load(asreview_filename, project_path)

    dataset_fp = Path(
        project_path, project.config["id"], "data", project.config["dataset_path"]
    )
    dataset = ASReviewData.from_file(dataset_fp)

    with open_state(asreview_filename) as state:
        df = state.get_dataset()
        # increasing screening number in exported notes column name
        # to avoid column name conflict while joining dataframes
        screening = 0
        for col in dataset.df.columns:
            if col == "exported_notes" or col == "labeling_order":
                screening = 0
            elif col.startswith("exported_notes"):
                try:
                    screening = int(col.split("_")[2])
                except IndexError:
                    screening = 0
        screening += 1

        df.rename(
            columns={
                "notes": f"exported_notes_{screening}",
                "label": f"Included_{screening}",
            },
            inplace=True,
        )

        if labeling_order:
            df[f"labeling_order_{screening}"] = df.index

            included_columns = [
                f"labeling_order_{screening}",
                f"Included_{screening}",
                f"exported_notes_{screening}",
            ]

        else:
            included_columns = [
                f"Included_{screening}",
                f"exported_notes_{screening}",
            ]

        dataset_with_results = dataset.df.join(
            df.set_index("record_id")[included_columns],
            on="record_id",
        )

    if only_with_notes:
        dataset_with_results = dataset_with_results[
            dataset_with_results[f"exported_notes_{screening}"].notna()
        ]

    dataset_with_results.to_csv(output_filename)

    shutil.rmtree(project_path)
