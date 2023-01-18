import shutil
from pathlib import Path

import pandas as pd
from asreview import open_state
from asreview import ASReviewProject
from asreview import ASReviewData

def export_notes(asreview_filename, mode="all", option="all"):
    project_path = Path("tmp_data")
    project_path.mkdir()
    project = ASReviewProject.load(asreview_filename, project_path)
    
    dataset_fp = Path(project_path, project.config['id'], "data", project.config['dataset_path'])
    dataset = ASReviewData.from_file(dataset_fp)
    # print(f'The dataset contains {len(dataset)} records.')
    print(dataset.to_dataframe().head())
    
    