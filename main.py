from __future__ import print_function

import fluidsim
import shutil

from fluidsim.solvers.ns2d.solver import Simul
params = Simul.create_default_params()


# print([attr for attr in dir(params) if not attr.startswith("_")])
# print(type(params.nu_2))
# print(type(params.output))
# print(params)

params.nu_2 = 1e-3
params.forcing.enable = False

params.init_fields.type = "noise"
params.output.periods_save.spatial_means = 1.0


sim = Simul(params)

# sim.time_stepping.start()

# shutil.rmtree(sim.output.path_run)

