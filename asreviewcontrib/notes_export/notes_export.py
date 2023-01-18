import shutil
from pathlib import Path
import os

from asreview import open_state
from asreview import ASReviewProject
from asreview import ASReviewData

def export_notes(asreview_filename, only_with_notes=False):
    project_path = Path("tmp_data")
    project_path.mkdir()
    project = ASReviewProject.load(asreview_filename, project_path)
    
    dataset_fp = Path(project_path, project.config['id'], "data", project.config['dataset_path'])
    dataset = ASReviewData.from_file(dataset_fp)

    project_path = Path("tmp_data")
    project_path.mkdir()
    project = ASReviewProject.load(asreview_filename, project_path)
    dataset_fp = Path(project_path, project.config['id'], "data", project.config['dataset_path'])
    dataset = ASReviewData.from_file(dataset_fp)
    
    outoutfile_name = os.path.basename(asreview_filename)
    outoutfile_name = f"{os.path.splitext(outoutfile_name)[0]}.csv"

    with open_state(asreview_filename) as state:
        df = state.get_dataset()
        df['labeling_order'] = df.index
        dataset_with_results = dataset.df.join(df.set_index('record_id')[['labeling_order','label','notes']])
        dataset_with_results.rename(columns={'labeling_order':'Ranking', 'label':'Included'}, inplace=True)
        
    if only_with_notes:
        dataset_with_results = dataset_with_results[dataset_with_results['notes'].notna()]
        
    dataset_with_results.to_csv(outoutfile_name, index=False)
    
    shutil.rmtree(project_path)
    
    