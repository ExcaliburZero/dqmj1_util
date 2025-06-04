.. _tutorial_modifying_data:

Modifying data
==============
In this tutorial, we will show you how to modify data in the game's ROM file using the :ref:`Raw Data API <raw_data>`.

Unlike the :ref:`Simple Data API <simple_data>` shown in :ref:`the previous tutorial <tutorial_reading_data>`, the Raw Data API allows you to modify and write data to the game's ROM.

Loading the ROM
---------------
First you will need to load in the ROM by creating a :class:`~dqmj1_util.Rom` object using the filepath where the ROM file is located.

For this it is recommended to use the North American version of the game.

.. code-block:: python

    import dqmj1_util as dqmj

    rom = dqmj.Rom("my_roms_folder/your_DQMJ1_NA_ROM_here.nds")

.. note::

    If you get a :code:`FileNotFoundError`, double check that the filepath to your ROM file is correct.

Reading raw data
----------------
Similar to reading data using the :ref:`Simple Data API <simple_data>`, as you've seen in :ref:`the previous tutorial <tutorial_reading_data>`, you can read raw data from the :class:`~dqmj1_util.Rom` object by accessing specific attributes.

Encounters
^^^^^^^^^^
By accessing the :attr:`~dqmj1_util.Rom.btl_enmy_prm` attribute, you can see information on each of the encounters in the game (enemy monster, gift monsters, starters, etc.).

.. code-block:: python

    >>> rom.btl_enmy_prm.entries[1]
    BtlEnmyPrmEntry(species_id=318, unknown_a=b'\x00\x00\x00\x01\x00\x00', skills=[BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=0), BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=100), BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=7), BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=171), BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=24), BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=181)], item_drops=[BtlEnmyPrmEntry.ItemDrop(item_id=0, chance_denominator_2_power=7), BtlEnmyPrmEntry.ItemDrop(item_id=0, chance_denominator_2_power=7)], gold=0, unknown_b=b'\x00\x00', exp=0, unknown_c=b'\x00\x00', level=40, unknown_d=0, unknown_e=0, scout_chance=0, max_hp=4065, max_mp=255, attack=336, defense=154, agility=92, wisdom=256, unknown_f=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', skill_set_ids=[0, 0, 0], unknown_g=b'\x00')
    >>> rom.btl_enmy_prm.entries[1].species_id
    318
    >>> rom.btl_enmy_prm.entries[1].skills[1]
    BtlEnmyPrmEntry.EnemySkill(unknown_a=0, skill_id=100)

.. note::

    Notice that compared to reading encounters data using the Simple Data API, the Raw Data API uses only ids (ex. :attr:`~dqmj1_util.raw.BtlEnmyPrmEntry.species_id`) and not names to refer to data such monster species and skills. This is because the raw data is a more direct conversion of the game's internal binary file formats, which typically do not contain any text directly.

    Additionally the Raw Data API has many cases of fields with names like :attr:`~dqmj1_util.raw.BtlEnmyPrmEntry.unknown_a`, :attr:`~dqmj1_util.raw.BtlEnmyPrmEntry.unknown_f`, etc.. These fields are used to represent parts of the game's data file formats that have not yet been figured out. Some of these fields are unused by the game while others have not yet had their specific purpose discovered. These fields may have their names and types changed once their purposes are better understood.

Skill sets
^^^^^^^^^^
By accessing the :attr:`~dqmj1_util.Rom.skill_tbl` attribute, you can see information on each of the skill sets in the game (ex. Frizz & Bang, Dark Knight, Attack Boost Ⅲ).

.. code-block:: python

    >>> rom.skill_tbl.entries[1]
    SkillTblEntry(can_upgrade=1, category=1, max_skill_points=50, skill_point_requirements=[3, 8, 15, 24, 36, 50, 50, 50, 50, 50], skill_ids=[[1], [84], [5], [86], [2, 1], [6, 5], [], [], [], []], trait_ids=[[], [], [], [], [], [], [], [], [], []], species_learnt_by=[243, 201])
    >>> rom.skill_tbl.entries[1].skill_point_requirements
    [3, 8, 15, 24, 36, 50, 50, 50, 50, 50]
    >>> rom.skill_tbl.entries[1].skill_ids
    [[1], [84], [5], [86], [2, 1], [6, 5], [], [], [], []]

Modifying and writing raw data
------------------------------
Once you have the ROM loaded and can read raw data from it, you can modify that raw data in order to create a new game ROM.

For example, here you can modify each of the encounters in the game to be Dr Snapped by setting the :attr:`~dqmj1_util.raw.BtlEnmyPrmEntry.species_id` for each encounter to 318 (Dr Snapped's species ID).

.. code-block:: python

    btl_enmy_prm = rom.btl_enmy_prm
    for btl in btl_enmy_prm.entries:
        btl.species_id = 318

Once you have made the changes you want to make to the game data, assign the modified data back to the ROM attribute you read it from and call the :meth:`~dqmj1_util.Rom.write` method to create a modified game ROM.

.. code-block:: python

    rom.btl_enmy_prm = btl_enmy_prm
    rom.write("oops_all_snaps.nds")

You can confirm that this worked by playing the newly created ROM file (:code:`oops_all_snaps.nds`) and upon picking your starter monster you should see that all 3 starter choices are Dr Snapped.