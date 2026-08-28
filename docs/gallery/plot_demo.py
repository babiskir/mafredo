"""
Read hyd and plot
==================

Minimum example

"""

from pathlib import Path

import matplotlib.pyplot as plt

from mafredo import Hyddb1, FrequencyUnit

file_name = Path(__file__).parent / "barge.hyd"
vessel = Hyddb1.create_from_hyd(filename=file_name)
vessel.plot(unit=FrequencyUnit.seconds, xlim=20)

plt.show()
