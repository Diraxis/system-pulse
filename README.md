# System Pulse

A lightweight CLI tool for monitoring system resource usage (CPU, memory, disk) and logging system state over time.

---

## Purpose

System Pulse is part of a broader effort to build **personal system control tools** — software that provides visibility, logging, and insight into machine behaviour.

---

## Features (Current)

* Real-time CPU, memory, and disk usage
* Terminal output refresh loop
* File-based logging (append mode)


---

## Planned Features

* Timestamped entries
* Log analysis (average, peak usage)
* Alerts (e.g., CPU > threshold)
* Modular structure (separate data, logging, analysis)
* CLI arguments (`--log`, `--analyze`)

---

## Tech Stack

* Python
* psutil
* CLI (Linux/Windows compatible)

---

## Usage

```bash
python3 system_pulse.py
```

---

## Project Status

Active development — early phase (focus: core functionality and reliability)

---

## Why This Project Exists

This is not just a utility.

It is part of building:

* system awareness
* automation capability
* system administration and networking (toward deeper system control)

---

## Author

**Diraxis**

"Building systems I can understand, control, and evolve."
