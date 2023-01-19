import argparse

from asreview.entry_points import BaseEntryPoint

from asreviewcontrib.notes_export.notes_export import export_notes

class ExportEntryPoint(BaseEntryPoint):
    description = "Exporting notes from ASReview with dataset"
    extension_name = "asreview-notes-export"

    @property
    def version(self):
        from asreviewcontrib.notes_export.__init__ import __version__
        return __version__

    def execute(self, argv):
        parser = argparse.ArgumentParser(prog='asreview notes_export')
        parser.add_argument("--only-with-notes",
                            action='store_true',
                            dest="only_with_notes",
                            help="Only include records with notes in the exported file")
       
        parser.add_argument('asreview_files',
                            metavar='asreview_files',
                            type=str,
                            nargs='+',
                            help='A (list of) ASReview files')
        
        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"asreview-notes-export: {self.version}",
        )

        args = parser.parse_args(argv)
        
        if len(args.asreview_files) > 1:
            raise ValueError("Exporting notes from multiple project files"
                            " via the CLI is not supported yet.")
                
        export_notes(
            asreview_filename=args.asreview_files[0],
            only_with_notes=args.only_with_notes
        )
        
        
