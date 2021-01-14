import sys 

def get_progress_bar():
    """
    This function returns the appropriate version of tqdm, as determined by
    tqdm.auto. If tqdm is not installed, an ImportError is raised.
    """
    try:
        from tqdm.auto import tqdm

        return tqdm
    except ImportError:
        raise ImportError(
            "tqdm must be installed to use a progress bar."
            "Either install tqdm or re-run with"
            "progress_bar = False"
        )

def ascii_progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()