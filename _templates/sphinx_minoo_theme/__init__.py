from __future__ import print_function
import os


"""SphinxMinooTheme.
https://github.com/saeiddrv/SphinxMinooTheme.
"""

class MinooVersion():
    major = "0"
    minor = "9"
    micro = "0"
    level = "Beta"
    release = r"2015/05/21"
    def info(self):
        return ".".join([self.major, self.minor, self.micro])
    def info_full(self):
        return (
            (
                (
                    (
                        (
                            (
                                (
                                    (
                                        (
                                            (
                                                (
                                                    f"major   = {self.major}"
                                                    + "\n"
                                                    + "minor   = "
                                                )
                                                + self.minor
                                            )
                                            + "\n"
                                        )
                                        + "micro   = "
                                    )
                                    + self.micro
                                )
                                + "\n"
                            )
                            + "level   = "
                        )
                        + self.level
                    )
                    + "\n"
                )
                + "release = "
            )
            + self.release
        ) + "\n"

__version__ = MinooVersion()


# From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
def get_html_theme_path():
    """Return list of HTML theme paths."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))




