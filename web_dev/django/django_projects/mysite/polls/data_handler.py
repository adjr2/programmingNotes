# %%
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from .db_handler import insert, connection


def extract_bench_data(fpathout):
    fpathout = Path(fpathout)
    bench = {
        "start": 0,
        "end": 0,
        "suite": "imb",
        "system": "SCC",
        "stdout": "",
        "stderr": "",
        "maxVal": 0.0,
    }
    if not fpathout.exists():
        print(f"Error: file'{fpathout}' does not exist!")
        # continue

    with open(fpathout) as resultout:
        resultout_lines = resultout.readlines()

    bench["stdout"] = "".join(resultout_lines)

    bench["data"] = imb_plot_data(resultout_lines, bench)

    add_times_and_id(resultout_lines, bench)
    return bench


def imb_plot_data(lines, bench):
    benchdata = {}
    benchname = ""

    for line in lines:
        benchre = re.search(r"^# Benchmarking (\S+)", line)
        if benchre:
            benchname = benchre.group(1)
        if benchname:
            benchaddon = re.search(r"^#    MODE: (\S+)", line)
            if benchaddon:
                benchname = benchname + " " + benchaddon.group(1)
            benchline = re.search(r"^\s+(\d+)\s+(\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)", line)
            if benchline:
                benchdata.setdefault(benchname, {})
                benchdata[benchname].setdefault("dataX", [])
                benchdata[benchname].setdefault("dataY", [])
                benchdata[benchname]["name"] = benchname
                benchdata[benchname]["labelX"] = "Bytes"
                benchdata[benchname]["labelY"] = "Mbytes/sec"
                benchdata[benchname]["dataX"].append(benchline.group(1))
                benchdata[benchname]["dataY"].append(benchline.group(4))
                bench["maxVal"] = (
                    benchline.group(4)
                    if float(benchline.group(4)) > float(bench["maxVal"])
                    else bench["maxVal"]
                )

    return benchdata


def add_times_and_id(lines, bench):
    for line in lines:
        start = re.search(r"^Started: (\S+)", line)
        if start:
            # print(datetime.strptime(start.group(1), "%Y-%m-%dT%H:%M:%S").strftime("%s"))
            bench["start"] = int(
                datetime.strptime(start.group(1), "%Y-%m-%dT%H:%M:%S").strftime("%s")
            )
            bench["job_date"] = datetime.strptime(
                start.group(1), "%Y-%m-%dT%H:%M:%S"
            ).strftime("%Y-%m-%dT%H:%M:%S")
        end = re.search(r"^Ended: (\S+)", line)
        if end:
            bench["end"] = int(
                datetime.strptime(end.group(1), "%Y-%m-%dT%H:%M:%S").strftime("%s")
            )
        jobid = re.search(r"^JobID = (\d+)", line)
        if jobid:
            bench["id"] = int(jobid.group(1))
    bench["runtime"] = int(bench["end"]) - int(bench["start"])


# %%
file_data = extract_bench_data("slurm.out")

# %%
con = connection("db.sqlite3")
for i, x_val in enumerate(file_data["data"]["PingPong"]["dataX"]):
    y_val = file_data["data"]["PingPong"]["dataY"][i]
    insert_data = [file_data["id"], file_data["job_date"], x_val, y_val]
    insert(con, "imb_pingpong", insert_data)
