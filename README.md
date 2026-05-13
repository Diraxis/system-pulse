# System Pulse

**System Pulse** is a lightweight CLI tool for monitoring and analyzing system resource usage over time.
It captures real-time CPU, memory, and disk data, persists it as structured logs, and extracts meaningful insights from historical behaviour.

---

## Why System Pulse?

Most system monitors show **what’s happening right now**.
System Pulse answers a more useful question:

> **“How does my machine behave over time?”**

It is designed as a foundational system introspection tool—small, observable, and extensible.

---

## Features

### 🔹 Real-Time Monitoring (Pulse Logger)

* Collects CPU, memory, and disk usage at regular intervals
* Displays live system state in the terminal
* Runs continuously with controlled refresh timing
* Gracefully handles user interruption (`Ctrl+C`)

---

### 🔹 Persistent Logging

* Writes timestamped system snapshots to `log.txt`
* Uses a consistent, structured log format
* Appends data without overwriting previous history

---

### 🔹 Log Analysis (Pulse Analyzer)

* Parses historical log data
* Extracts CPU, memory, and disk usage values
* Computes:

  * **Average usage** → baseline system behaviour
  * **Peak usage** → stress conditions
* Outputs summary statistics and monitoring duration

---

### 🔹 Robust Data Handling

* Skips malformed or incomplete log entries
* Handles corrupted or non-numeric values safely
* Prevents crashes on empty or invalid log files

---

### 🔹 Modular Design

System Pulse is structured around clear responsibilities:

* **Data Collection** → `usage.py`
* **Formatting** → `log_utils.py`
* **Logging** → `pulse_logger.py`
* **Analysis** → `pulse_analyzer.py`

This separation enables:

* Easier debugging
* Safer refactoring
* Scalable feature expansion

---

## File Structure

```text
system-pulse/
├── pulse_logger.py     # Entry point: real-time logging loop
├── pulse_analyzer.py   # Entry point: log analysis
├── usage.py            # System metrics collection (CPU, memory, disk)
├── log_utils.py        # Log formatting and parsing helpers
├── log.txt             # Generated at runtime
└── README.md
```

---

## Usage

### Run Logger

```bash
python pulse_logger.py
```

* Press `Ctrl+C` to stop
* Logs are written to `log.txt`

---

### Run Analyzer

```bash
python pulse_analyzer.py
```

---

## Example Output

```text
Monitoring duration : 0h 6m 0s
Entries logged      : 120
Average CPU         : 12.4%
Peak CPU            : 68.2%
Average Memory      : 45.1%
Peak Memory         : 72.3%
Average Disk        : 61.0%
Peak Disk           : 61.0%
```

---

## Design Approach

System Pulse was built using a **progressive systems approach**:

* **v1** → Real-time monitoring (stateless output)
* **v2** → Persistent logging (state over time)
* **v3** → Data parsing and analysis
* **v4** → Modular architecture and separation of concerns

Each phase focused on:

> building → understanding → stress testing → refining

---

## Known Limitations

* Log parsing depends on a consistent format
* Multiple logger instances may interleave entries
* Editing the log file during execution can cause partial data loss
* Analysis is currently aggregate-only (no time-based segmentation)

---

## Roadmap

* [X] Basic timestamp-based analysis (monitoring duration)
* [ ] Time-window analysis and trends
* [ ] Real-time analyzer (rolling averages)
* [ ] Alert system (e.g., CPU > 80%)
* [ ] CLI arguments (`--log`, `--analyze`)
* [ ] Package-level structure (`system_pulse/` module)

---

## What This Project Demonstrates

* File I/O and structured logging
* Data parsing and validation
* Defensive programming (error handling)
* Separation of concerns and modular design
* Iterative system development

---

## Author

**Diraxis**
*“Building systems I can understand, control, and evolve.”*
