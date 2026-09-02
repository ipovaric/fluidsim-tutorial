from __future__ import print_function

import fluidsim
import shutil

from fluidsim.solvers.ns2d.solver import Simul
from fluidsim import load_sim_for_plot
from fluidsim import load_state_phys_file

params = Simul.create_default_params()

sim = Simul(params)

# sim.time_stepping.start()

sim = load_state_phys_file(r"C:\\Users\\ipova\\Sim_data\\NS2D_48x48_S8x8_2026-09-01_20-36-27")

# sim.output.spatial_means.plot()
sim.output.phys_fields.plot()

# shutil.rmtree(sim.output.path_run)

