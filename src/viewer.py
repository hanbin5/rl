import numpy as np

import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("../model/model.xml")
data = mujoco.MjData(model)

mujoco.viewer.launch(model, data)