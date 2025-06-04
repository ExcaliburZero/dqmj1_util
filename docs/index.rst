.. dqmj1_util documentation master file, created by
   sphinx-quickstart on Sun Jun  1 20:11:01 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DQMJ1 Utilities (:code:`dqmj1_util`)
====================================
.. toctree::
   :maxdepth: 2
   :hidden:

   tutorials/index
   simple_data/index
   raw_data/index
   api_documentation/index

DQMJ1 Utilities is an unofficial Python library for parsing a modifying data files from Dragon Quest Monsters: Joker.

This library is a work in progress, so the API may change frequently.

.. code-block:: python

   import dqmj1_util as dqmj

   rom = dqmj.Rom("Dragon Quest Monsters - Joker (USA).nds")

   # Reading game data
   encounters = rom.encounters
   print(encounters[1].species)
   print(encounters[1].species_id)

   # Modding game files
   btl_enmy_prm = rom.btl_enmy_prm
   for btl in btl_enmy_prm.entries:
      btl.species_id = 318  # 318 == Dr Snapped

   rom.btl_enmy_prm = btl_enmy_prm
   rom.write("oops_all_snaps.nds")

Sections
--------
* :ref:`Tutorials <tutorials>` walks you through using :code:`dqmj1_util` to read and modify data from the game's ROM.
* :ref:`Simple Data <simple_data>` teaches you about reading data from the game in a simple but read-only way.
* :ref:`Raw Data <raw_data>` teaches you about reading and writing raw data from the game's ROM.
* :ref:`API Documentation <api_documentation>` gives you details on the classes, methods, etc. offered by the library.