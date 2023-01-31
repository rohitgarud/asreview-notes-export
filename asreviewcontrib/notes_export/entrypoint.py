import argparse
import os
from datetime import datetime

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
        parser = argparse.ArgumentParser(prog="asreview notes_export")
        parser.add_argument(
            "--only-with-notes",
            action="store_true",
            dest="only_with_notes",
            help="Only include records with notes in the exported file",
        )

        parser.add_argument(
            "asreview_files",
            metavar="asreview_files",
            type=str,
            nargs="+",
            help="A (list of) ASReview files",
        )

        parser.add_argument(
            "-V",
            "--version",
            action="version",
            version=f"asreview-notes-export: {self.version}",
        )

        parser.add_argument(
            "-o",
            "--output",
            dest="outputfile_name",
            help="Output file name or path. Currently only .csv files are supported.",
        )

        args = parser.parse_args(argv)

        if len(args.asreview_files) > 1:
            raise ValueError(
                "Exporting notes from multiple project files"
                " via the CLI is not supported yet."
            )

        asreview_filename = args.asreview_files[0]

        if args.outputfile_name:
            outputfile_name = args.outputfile_name
            if not outputfile_name.endswith(".csv"):
                if "." in outputfile_name:
                    raise ValueError(
                        "File extensions other than .csv are not supported yet"
                    )
                else:
                    outputfile_name += ".csv"
        else:
            outputfile_name = os.path.basename(asreview_filename)
            outputfile_name = f"{os.path.splitext(outputfile_name)[0]}-{datetime.now().strftime('%Y%m%dT%H%M')}.csv"

        export_notes(
            asreview_filename=asreview_filename,
            output_filename=outputfile_name,
            only_with_notes=args.only_with_notes,
        )
