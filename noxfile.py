from pathlib import Path

import nox

ROOT = Path(__file__).parent
PELICAN = ROOT / "pelican"
OUTPUT = ROOT / "output"

nox.options.default_venv_backend = "uv"
nox.options.sessions = []


PYTHON = "3.13"


def session(default=True, python=PYTHON, **kwargs):  # noqa: D103
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(python=python, **kwargs)(fn)

    return _session


@session(default=False)
def develop(session):
    session.run(
        "uv",
        "run",
        "--active",
        "pelican",
        "--delete-output-directory",
        "-s",
        PELICAN / "pelicanconf.py",
        *session.posargs,
    )


@session(default=False)
def build(session):
    session.run(
        "uv",
        "run",
        "--active",
        "pelican",
        "-s",
        PELICAN / "publishconf.py",
        "--fatal",
        "warnings",
        *session.posargs,
    )


@session(default=False)
def ui(session):
    session.run(
        "uv",
        "--with=twisted",
        "run",
        "twist",
        "web",
        "--path",
        OUTPUT,
    )
