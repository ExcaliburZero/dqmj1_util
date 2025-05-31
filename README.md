# DQMJ1 Utilities [![Test](https://github.com/ExcaliburZero/dqmj1_util/actions/workflows/test.yml/badge.svg)](https://github.com/ExcaliburZero/dqmj1_util/actions/workflows/test.yml) [![Coverage Status](https://coveralls.io/repos/github/ExcaliburZero/dqmj1_util/badge.svg?branch=main)](https://coveralls.io/github/ExcaliburZero/dqmj1_util?branch=main) [![Maintainability](https://qlty.sh/badges/e7b9e8a5-bfb0-4e03-bd74-7ab53fffdfb8/maintainability.svg)](https://qlty.sh/gh/ExcaliburZero/projects/dqmj1_util)
An unofficial library for parsing a modifying data files from *Dragon Quest Monsters: Joker*.

This library is a work in progress, so the API may change frequently.

```python
import dqmj1_util as dqm

encounters = dqm.Rom("DQMJ1_NA.nds").load_btl_enmy_prm()

print(encounters.entries[1].species_id)
```