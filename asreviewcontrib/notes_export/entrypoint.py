import argparse
import shutil
from pathlib import Path
import os

import pandas as pd
from asreview import ASReviewProject
from asreview import ASReviewData

from asreview import open_state
from asreview.entry_points import BaseEntryPoint


class ExportEntryPoint(BaseEntryPoint):
    description = "Exporting notes from ASReview with dataset"
    extension_name = "asreview-notes-export"

    @property
    def version(self):
        from asreviewcontrib.notes_export.__init__ import __version__
        return __version__

    def execute(self, argv):
        parser = argparse.ArgumentParser(prog='asreview notes-export')
        parser.add_argument("export_type",
                            metavar='type',
                            type=str,
                            default="all",
                            help="")
        
        parser.add_argument('asreview_file',
                            metavar='asreview_file',
                            type=str,
                            nargs='+',
                            help='ASReview file')

        args = parser.parse_args(argv)
        
        project_path = Path("tmp_data")
        project_path.mkdir()
        project = ASReviewProject.load(args.asreview_file, project_path)
        dataset_fp = Path(project_path, project.config['id'], "data", project.config['dataset_path'])
        dataset = ASReviewData.from_file(dataset_fp)
        
        outoutfile_name = os.path.basename(args.asreview_file)
        outoutfile_name = f"{os.path.splitext(outoutfile_name)[0]}.csv"

        with open_state(args.asreview_file) as state:
            df = state.get_dataset()
            df['labeling_order'] = df.index
            dataset_with_results = dataset.df.join(df.set_index('record_id')[['labeling_order','label','notes']])
            dataset_with_results.rename(columns={'labeling_order':'Ranking', 'label':'Included'}, inplace=True)
            dataset_with_results.to_csv(outoutfile_name, index=False)

        shutil.rmtree(project_path)