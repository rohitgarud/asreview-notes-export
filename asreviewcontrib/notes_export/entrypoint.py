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
       
        parser.add_argument('asreview_file',
                            metavar='asreview_file',
                            type=str,
                            nargs='+',
                            help='ASReview file')

        args = parser.parse_args(argv)
        
        print(args.asreview_file)
        
        export_notes(
            asreview_filename=args.asreview_file,
            only_with_notes=args.only_with_notes
        )
        
        
