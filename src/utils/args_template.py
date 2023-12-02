
from enum import Enum 
from collections import namedtuple

ArgTemplate = namedtuple('ArgTemplate', ['name_or_flags', 'type', 'default', 'choices', 'help'])

ARGUMENT_TEMPLATES = [
    ArgTemplate(name_or_flags="--level", type=str, default="info", choices=["debug", "info", "warning", "error", "critical"], help="Select one of logging configs (debug, info, warning, error, critical) by default info"),
    ArgTemplate(name_or_flags="--verbose", type=str, default="false", choices=["true", "false"], help="This will output all log messages to the console")
]