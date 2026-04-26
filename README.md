# System Pulse

A lightweight CLI tool for monitoring and analyzing system resource usage over time.

---

## Overview

System Pulse captures CPU, memory, and disk usage in real time, logs system state to a file, and analyzes historical data to extract meaningful insights.

---

## Features

### Logging (Pulse Logger)

* Real-time CPU, memory, and disk monitoring
* Continuous refresh loop
* Timestamped log entries written to file

### Analysis (Pulse Analyzer)

* Parses logged data
* Computes:

  * Average usage
  * Peak usage
* Summarizes system behaviour over time

---

## File Structure

```
pulse_logger.py     # Collects system data and writes logs
pulse_analyzer.py   # Parses logs and computes insights
usage.py            # System usage data collection (CPU, memory, disk)
log_utils.py        # Log formatting utilities
log.txt             # Generated at runtime
```

---

## Usage

### Run Logger

```bash
python pulse_logger.py
```

* Press `Ctrl+C` to stop
* Data is written to `log.txt`

---

### Run Analyzer

```bash
python pulse_analyzer.py
```

---

## Example Output

```
Entries logged : 120
Average CPU    : 12.4%
Peak CPU       : 68.2%
Average Memory : 45.1%
Peak Memory    : 72.3%
Average Disk   : 61.0%
Peak Disk      : 61.0%
```

---

## Known Limitations

* Log parsing depends on consistent log format
* Concurrent logger instances may interleave entries
* Editing the log file during execution can cause partial data loss

---

## Roadmap

* [ ] Handle malformed log entries safely
* [ ] Add timestamp-based analysis (time windows, trends)
* [ ] Implement alert thresholds (e.g., CPU > 80%)
* [ ] Improve modular structure (separate core components)

---

## Purpose

System Pulse is part of a broader effort to build tools for:

* system visibility
* behavioural analysis over time
* controlled, observable computing environments

---

## Author

Diraxis
"Building systems I can understand, control, and evolve."
