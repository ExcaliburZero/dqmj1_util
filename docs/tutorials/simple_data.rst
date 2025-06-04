.. _tutorial_reading_data:

Reading data
============
In this tutorial, we will show you how to read data from the game's ROM file using the :ref:`Simple Data API <simple_data>`.

Loading the ROM
---------------
First you will need to load in the ROM by creating a :class:`~dqmj1_util.Rom` object using the filepath where the ROM file is located.

For this it is recommended to use the North American version of the game.

.. code-block:: python

    import dqmj1_util as dqmj

    rom = dqmj.Rom("my_roms_folder/your_DQMJ1_NA_ROM_here.nds")

.. note::

    If you get a :code:`FileNotFoundError`, double check that the filepath to your ROM file is correct.

Reading specific data types
---------------------------
Once you have a ROM loaded, you can read specific types of data from the game by accessing specific attributes of the :class:`~dqmj1_util.Rom` object.

Encounters
^^^^^^^^^^
By accessing the :attr:`~dqmj1_util.Rom.encounters` attribute, you can see information on each of the encounters in the game (enemy monster, gift monsters, starters, etc.).

.. code-block:: python

    >>> rom.encounters[1]
    Encounter(species='Dr Snapped', species_id=318, skills=['Attack', 'Uncarnate', 'Kaboom', 'Disruptive Wave', 'Kazammle', 'Meditation'], skill_ids=[0, 100, 7, 171, 24, 181], item_drops=[], item_drop_item_ids=[], gold=0, exp=0, level=40, scout_chance=0, max_hp=4065, max_mp=255, attack=336, defense=154, agility=92, wisdom=256, skill_sets=[], skill_set_ids=[])
    >>> rom.encounters[1].species
    'Dr Snapped'
    >>> rom.encounters[1].skills
    ['Attack', 'Uncarnate', 'Kaboom', 'Disruptive Wave', 'Kazammle', 'Meditation']

Skill sets
^^^^^^^^^^
By accessing the :attr:`~dqmj1_util.Rom.skill_sets` attribute, you can see information on each of the skill sets in the game (ex. Frizz & Bang, Dark Knight, Attack Boost Ⅲ).

.. code-block:: python

    >>> rom.skill_sets[0]
    SkillSet(name='Frizz & Bang', can_upgrade=True, category=1, max_skill_points=50, rewards=[SkillSet.Reward(skill_point_requirement=3, skill='Frizz', skill_id=1, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=8, skill='Flame Slash', skill_id=84, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=15, skill='Bang', skill_id=5, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=24, skill='Bomb Slash', skill_id=86, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=36, skill='Frizzle', skill_id=2, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=50, skill='Boom', skill_id=6, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=50, skill=None, skill_id=None, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=50, skill=None, skill_id=None, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=50, skill=None, skill_id=None, trait=None, trait_id=None), SkillSet.Reward(skill_point_requirement=50, skill=None, skill_id=None, trait=None, trait_id=None)], species_learnt_by=[243, 201], species_learnt_by_ids=[])
    >>> rom.skill_sets[0].name
    'Frizz & Bang'
    >>> rom.skill_sets[0].rewards[0]
    SkillSet.Reward(skill_point_requirement=3, skill='Frizz', skill_id=1, trait=None, trait_id=None)

