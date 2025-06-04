Parsing simple data
===================
In this tutorial, we will show you how to read data from the game's ROM file using the :ref:`Simple Data API <simple_data>`.

Loading the ROM
---------------
First you will need to load in the ROM by creating a :class:`Rom` object using the filepath where the ROM file is located.

For this it is recommended to use the North American version of the game.

.. code-block:: python

    import dqmj1_util as dqmj

    rom = dqmj.Rom("my_roms_folder/your_DQMJ1_NA_ROM_here.nds")

.. note::

    If you get a :code:`FileNotFoundError`, double check that the filepath to your ROM file is correct.