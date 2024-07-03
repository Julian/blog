from pathlib import Path

import nox

ROOT = Path(__file__).parent
PELICAN = ROOT / "pelican"
OUTPUT = ROOT / "output"

REQUIREMENTS = dict(
    main=ROOT / "requirements.txt",
)
REQUIREMENTS_IN = [  # this is actually ordered, as files depend on each other
    (path.parent / f"{path.stem}.in", path) for path in REQUIREMENTS.values()
]

SUPPORTED = ["3.12"]
LATEST = SUPPORTED[-1]

nox.options.default_venv_backend = "uv|virtualenv"
nox.options.sessions = []


def session(default=True, python=LATEST, **kwargs):  # noqa: D103
    def _session(fn):
        if default:
            nox.options.sessions.append(kwargs.get("name", fn.__name__))
        return nox.session(python=python, **kwargs)(fn)

    return _session


@session(default=False)
def develop(session):
    session.install("-r", REQUIREMENTS["main"])
    session.run(
        "pelican",
        "--delete-output-directory",
        "-s",
        PELICAN / "pelicanconf.py",
        *session.posargs,
    )


@session(default=False)
def build(session):
    session.install("-r", REQUIREMENTS["main"])
    session.run(
        "pelican",
        "-s",
        PELICAN / "publishconf.py",
        "--fatal",
        "warnings",
        *session.posargs,
    )


@session()
def audit(session):
    """
    Audit dependencies for vulnerabilities.
    """
    session.install("pip-audit", "-r", REQUIREMENTS["main"])
    session.run("python", "-m", "pip_audit")


@session(default=False)
def ui(session):
    session.install("twisted")
    session.run("twist", "web", "--path", OUTPUT)


@session(default=False)
def requirements(session):
    """
    Update the project's pinned requirements.

    You should commit the result afterwards.
    """
    if session.venv_backend == "uv":
        cmd = ["uv", "pip", "compile"]
    else:
        session.install("pip-tools")
        cmd = ["pip-compile", "--resolver", "backtracking", "--strip-extras"]

    for each, out in REQUIREMENTS_IN:
        # otherwise output files end up with silly absolute path comments...
        relative = each.relative_to(ROOT)
        session.run(*cmd, "--upgrade", "--output-file", out, relative)
