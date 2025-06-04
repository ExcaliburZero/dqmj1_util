# DQMJ1 Utilities [![Test](https://github.com/ExcaliburZero/dqmj1_util/actions/workflows/test.yml/badge.svg)](https://github.com/ExcaliburZero/dqmj1_util/actions/workflows/test.yml) [![Coverage Status](https://coveralls.io/repos/github/ExcaliburZero/dqmj1_util/badge.svg?branch=main)](https://coveralls.io/github/ExcaliburZero/dqmj1_util?branch=main) [![Maintainability](https://qlty.sh/badges/e7b9e8a5-bfb0-4e03-bd74-7ab53fffdfb8/maintainability.svg)](https://qlty.sh/gh/ExcaliburZero/projects/dqmj1_util) [![Documentation](https://readthedocs.org/projects/dqmj1_util/badge/?version=latest)](https://dqmj1-util.readthedocs.io/en/latest/)

An unofficial library for parsing a modifying data files from _Dragon Quest Monsters: Joker_.

This library is a work in progress, so the API may change frequently.

```python
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
```

## Documentation

For information on how to use the library, see the documentation at:

<https://dqmj1-util.readthedocs.io/en/latest/>
