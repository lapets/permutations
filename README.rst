============
permutations
============

Python library for instantiating and working with permutation collections that provide efficient implementations of all sequence methods (including random-access retrieval by index).

|pypi|

.. |pypi| image:: https://badge.fury.io/py/permutations.svg
   :target: https://badge.fury.io/py/permutations
   :alt: PyPI version and link.

Purpose
-------

.. |itertools_permutations| replace:: ``itertools.permutations``
.. _itertools_permutations: https://docs.python.org/3/library/itertools.html#itertools.permutations

.. |Sequence| replace:: ``Sequence``
.. _Sequence: https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence

This library provides a drop-in alternative to the built-in |itertools_permutations|_ function that also implements the features of a |Sequence|_, including the ability to access individual entries using the index (without iterating over all permutations up to that point).

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/permutations>`__:

.. code-block:: bash

    python -m pip install permutations

The library can be imported in the usual ways:
                              
.. code-block:: python

    import permutations
    from permutations import permutations

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``lint``) when performing installation using `pip <https://pypi.org/project/pip>`__:

.. code-block:: bash

    python -m pip install .[lint]

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details):

.. code-block:: bash

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__:

.. code-block:: bash

    python src/permutations/permutations.py -v

Style conventions are enforced using `Pylint <https://pylint.readthedocs.io>`__:

.. code-block:: bash

    python -m pip install .[lint]
    python -m pylint src/permutations

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/permutations>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/permutations>`__ by a package maintainer. First, install the dependencies required for packaging and publishing:

.. code-block:: bash

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``. Create and push a tag for this version (replacing ``?.?.?`` with the version number):

.. code-block:: bash

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive:

.. code-block:: bash

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__:

.. code-block:: bash

    python -m twine upload dist/*