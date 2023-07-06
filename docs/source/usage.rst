Usage
=====

.. _installation:

Installation
------------

To use Sphinx, first install it using pip:

.. code-block:: console

    (.venv) $ pip install sphinx

To start creating documentation, run the following command:

.. code-block:: console

    sphinx-quickstart docs

> Separate source and build directories (y/n) [n]: Write "y" (without quotes) and press Enter.

> Project name: Write "Lumache" (without quotes) and press Enter.

> Author name(s): Write "Graziella" (without quotes) and press Enter.

> Project release []: Write "0.1" (without quotes) and press Enter.

> Project language [en]: Leave it empty (the default, English) and press Enter.

.. code-block:: console

    sphinx-build -b html docs/source/ docs/build/html


An example of documenting code objects in Python language:

Print value
-----------

To print the value of a variable, you can use the ``print()`` function:

.. py:function:: print(value=None)

    Return the value of the variable passed in the bracket.

    :param value: Optional variable.
    :type value: int, float, str, list[str] or None
    :raise StringError: If the value is invalid.
    :return: The value of the variable.
    :rtype: list[str]

The ``value`` parameter should be either ``[str]`` with single quotation marks ``''`` or double quotations mark ``""``. Otherwise, :py:func:`print()` will raise an exception.

.. py:exception:: StringError

    Raised if the value is not enclosed in single quotations mark or double quotations mark.

Host Sphinx documentation from servers:

1. GitHub Pages
2. Read The Docs

.. note::

    This project is under active development.
