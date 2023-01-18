import argparse

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
        
        parser.add_argument('asreview_files',
                            metavar='asreview_files',
                            type=str,
                            nargs='+',
                            help='A (list of) ASReview files.')

        args = parser.parse_args(argv)

        if len(args.asreview_files) > 1:
            raise ValueError("Exporting notes from multiple project files via the CLI is not supported yet.")

        with open_state(args.asreview_files[0]) as s:
            pass
