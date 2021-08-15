import library.const as g


def log(text, level=1, name="WDM", *arg, **kwargs):
    """Emitting the log message."""
    g.LOG.info("[" + name + "] - " + text)
