# Chronolapse Multi-Window Capture Architecture

## Overview
This document outlines the architecture and roadmap for the OBS-style multi-window targeting system in this Chronolapse fork. By default, Chronolapse only recorded the entire screen. We are expanding its core functionality to capture specific, individual software windows simultaneously based on their window name or handle, completely ignoring the desktop background.

This fork is strictly targeting Windows.

## Target Applications
Our initial target applications for multi-window capture include:
- Jules
- GitHub Desktop
- RPG Maker

## Roadmap

### Phase 1: Core Logic via Configuration (Complete)
- **Objective:** Implement core multi-window capture logic driven strictly by the `chronolapse.config` file.
- **Technology Stack:** Python, `win32gui`, and `mss`.
- **Functionality:**
  - Read a user-defined list of target window names via the `target_windows` parameter in the configuration file.
  - Fetch exact coordinates and bounding boxes of specific open windows dynamically. *Implemented `win32gui.GetWindowRect()` to isolate captures to specific window coordinates.*
  - Iterate through the target list in the core capture loop.
  - Save captures as parallel image sequences with the window name appended to the filename (e.g., `prefix_WindowName_0001.jpg`).
- **UI:** No changes to the GUI in this phase.

### Phase 2: GUI Integration (Active)
- **Objective:** Integrate the new configuration options directly into the wxPython GUI (`chronolapsegui.py` / `chronolapsegui.wxg`).
- **Functionality:**
  - Add UI elements (checkboxes, text fields, or lists) to allow users to add, edit, and remove target windows from within the application.
  - Expose any relevant compositing or output formatting options visually.