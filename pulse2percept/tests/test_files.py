import numpy as np
import numpy.testing as npt
import pytest
import os

from pulse2percept import files


def test_savemoviefiles():
    # This function is deprecated
    try:
        from PIL import Image
    except ImportError:
        # If PIL is not installed, running savemoviefiles should break
        with pytest.raises(AssertionError):
            files.savemoviefiles("blah.avi", np.zeros(10), path='./')
    else:
        # Avoid import but unused error
        Image.__name__

        if os.name != 'nt':
            # If not on Windows, this should break
            with pytest.raises(OSError):
                files.savemoviefiles("blah.avi", np.zeros(10), path='./')
        else:
            # smoke test
            files.savemoviefiles("blah.avi", np.zeros(10), path='./')


def test_npy2movie():
    # This function is deprecated
    try:
        from PIL import Image
    except ImportError:
        # If PIL is not installed, running savemoviefiles should break
        with pytest.raises(AssertionError):
            files.npy2movie("blah.avi", np.zeros(10))
    else:
        # Avoid import but unused error
        Image.__name__

        if os.name != 'nt':
            # If not on Windows, this should break
            with pytest.raises(OSError):
                files.npy2movie("blah.avi", np.zeros(10))
        else:
            # smoke test
            files.npy2movie("blah.avi", np.zeros(10))


def test_scale():
    # This function is deprecated
    inarray = np.random.rand(100)
    for newmin in [0.0, -0.5]:
        for newmax in [1.0, 10.0]:
            scaled = files.scale(inarray, newmin=newmin, newmax=newmax)
            npt.assert_almost_equal(scaled.min(), newmin)
            npt.assert_almost_equal(scaled.max(), newmax)


def test_find_files_like():
    # Not sure how to check a valid pattern match, because we
    # don't know in which directory the test suite is
    # executed... so smoke test
    files.find_files_like(".", ".*")

    # Or fail to find an unlikely file name
    filenames = files.find_files_like(".", "theresnowaythisexists\.xyz")
    npt.assert_equal(filenames, [])
