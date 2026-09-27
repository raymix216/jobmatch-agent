"""CLI entrypoint: `python -m jobmatch <command>`."""

import argparse
import sys

from jobmatch import __version__
from jobmatch.config import settings


def cmd_health(_args: argparse.Namespace) -> int:
    print(f"{settings.app_name} v{__version__} — OK")
    return 0


def cmd_version(_args: argparse.Namespace) -> int:
    print(__version__)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="jobmatch", description="JobMatch Agent")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health", help="config loads and process starts").set_defaults(
        func=cmd_health
    )
    sub.add_parser("version", help="print version").set_defaults(func=cmd_version)
    # M1: ingest, score
    # M2: route, eval
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
