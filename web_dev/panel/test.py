# %%
# %pip install panel
# %pip install jupyter_bokeh
# %pip install virtualenv
# %pip install matplotlib

# %%
# import bokeh
import panel as pn

pn.extension()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#### HPCG ####
with open("HPCG-Benchmark_3.1_2022-12-03_14-24-54.txt") as file:
    lines = file.readlines()

#%%
import re

data_dict = {}
multigrid_dict = {}
coarsegrid_dict = {}

key = ""
for line in lines:
    if re.search("=$", line):
        if "#" not in line:
            key = line.split("=")[0]
            # print(key)
            inner_data_dict = {}

    if "::".join(line.split("::")[:-1]) == "Multigrid Information::Coarse Grids":
        if "Grid" in line.split("::")[2].split("=")[0]:
            multigrid_key = line.split("::")[2].replace("\n", "")
            multigrid_dict[multigrid_key] = []
            continue
        multigrid_dict[multigrid_key].append(line.split("::")[2].replace("\n", ""))
        continue

    if "::".join(line.split("::")[:-1]) == "Memory Use Information::Coarse Grids":
        if "Grid" in line.split("::")[2].split("=")[0]:
            coarsegrid_key = line.split("::")[2].replace("\n", "")
            coarsegrid_dict[coarsegrid_key] = []
            continue
        coarsegrid_dict[coarsegrid_key].append(line.split("::")[2].replace("\n", ""))
        continue

    if "::".join(line.split("::")[:-1]) == key:
        if len(line.split("::")) == 3:
            inner_key = line.split("::")[2].split("=")[0]

            inner_data_dict[inner_key] = (
                line.split("::")[2].split("=")[1].replace("\n", "")
            )
            data_dict[key] = inner_data_dict

        if len(line.split("::")) == 2:
            inner_key = line.split("::")[1].split("=")[0]

            inner_data_dict[inner_key] = (
                line.split("::")[1].split("=")[1].replace("\n", "")
            )
            data_dict[key] = inner_data_dict

data_dict["Multigrid Information::Coarse Grids"] = multigrid_dict
data_dict["Memory Use Information::Coarse Grids"] = coarsegrid_dict

#%%
import pickle

# pickle.dump(data_dict, open("data_dict.txt", "w"))
with open("data_dict.txt", "wb") as file1:
    pickle.dump(data_dict, file1)
# inner_data_dict2

#%%
# import numpy as np
# import matplotlib.pyplot as plt

# test_plot_data = data_dict["Machine Summary"]

# fig, axs = plt.subplots(1, 1)
# columns = ("Column I", "Column II")
# the_table = axs.table(
#     cellText=[list(test_plot_data.keys()), list(test_plot_data.values())],
#     colLabels=columns,
#     loc="center",
# )
# axs.xaxis.set_visible(False)
# axs.yaxis.set_visible(False)
# fig.tight_layout()
# plt.show()

#%%
# %pip install plottable
