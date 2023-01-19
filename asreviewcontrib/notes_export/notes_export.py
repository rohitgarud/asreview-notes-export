import shutil
from pathlib import Path

from asreview import open_state
from asreview import ASReviewProject
from asreview import ASReviewData

def export_notes(asreview_filename, outputfile_name, only_with_notes=False):
    """Export notes with data from ASReview file
            Parameters
            ----------
            asreview_filename: str,
                File name of ASreview file with .asreview extension
                
            only_with_notes: bool,
                Flag if True exports only records with notes to dataset csv
            
            Returns
            -------
            None
            
            csv file is generated in the current directory
    """
    project_path = Path("tmp_data")
    project_path.mkdir(parents=True, exist_ok=True)
    project = ASReviewProject.load(asreview_filename, project_path)
    
    dataset_fp = Path(project_path, project.config['id'], "data", project.config['dataset_path'])
    dataset = ASReviewData.from_file(dataset_fp)
   
    with open_state(asreview_filename) as state:
        df = state.get_dataset()
        df['labeling_order'] = df.index
        df.rename(columns={'notes':'exported_notes'}, inplace=True)
        
        dataset_with_results = dataset.df.join(df.set_index('record_id')[['labeling_order','label','exported_notes']], on='record_id')
        dataset_with_results.rename(columns={'label':'Included'}, inplace=True)
        
    if only_with_notes:
        dataset_with_results = dataset_with_results[dataset_with_results['exported_notes'].notna()]

    dataset_with_results.to_csv(outputfile_name)

    shutil.rmtree(project_path)
    
    