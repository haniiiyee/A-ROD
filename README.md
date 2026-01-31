# A-ROD: Autonomous Relative Orbit Determination 🛰️🛡️

> **"In orbital rendezvous, data is never reliable on its own: it only makes sense when put in tension with a dynamic model."** — *Industry feedback on the A-ROD architecture.*

### The Problem: The "Trust Gap"
In space, sensors are liars. Standard GNSS signals jitter and drift by meters, providing a chaotic "uncertainty cloud" rather than a clean path. For a docking mission like **ISRO's SpaDeX**, trusting these raw "lies" would lead to a mission-ending collision.

### The Solution: A-ROD Engine
I architected A-ROD to act as a **mathematical gatekeeper**. It doesn't just "smooth" the noise; it arbitrates between what the sensors suggest and what the laws of physics allow.

---

## 🏗️ Technical Architecture
Instead of following data points blindly, the system enforces a **hierarchy of constraints**.

* **Physics-First Modeling**: Utilized **Clohessy-Wiltshire dynamics** to model relative motion in the **LVLH frame**. This ensures the chaser satellite adheres to unbreakable orbital invariants.
* **The Estimator**: Implemented an **Extended Kalman Filter (EKF)** using the **Joseph Form Covariance Update**. This ensures numerical stability on flight-grade hardware, preventing mathematical divergence.
* **Passive Safety**: Designed around a **Safety Ellipse**. This is a fail-safe geometry: if the satellite loses all power, natural orbital physics keep it circling safely rather than drifting into a crash.

---

## 📈 Performance Metrics
| Metric | Raw Sensor Data | A-ROD (EKF) Result |
| :--- | :--- | :--- |
| **Position Jitter** | ±3–5 meters | **Sub-meter accuracy** |
| **Trajectory** | Stochastic/Jagged | **Smooth/Physics-Verified** |
| **Safety Risk** | High (Collision Course) | **Fail-Safe (Closed Loop)** |

---

## 🤖 Workflow & Philosophy
I served as the **System Architect**, defining the mathematical framework and safety protocols. I utilized **AI as a "Co-Pilot"** to handle boilerplate implementation, allowing me to focus on high-level mission logic and numerical stability.

---

## 🚀 Developer
**Hani Mohammad Kaif** Electronics and Communication Engineering | St. Joseph Engineering College