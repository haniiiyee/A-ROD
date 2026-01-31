# A-ROD: Finding Truth in Orbital Chaos 🛰️🛡️

> **"In orbital rendezvous, data is never reliable on its own: it only makes sense when put in tension with a dynamic model."** — *Industry feedback on the A-ROD architecture.*

### The Problem: The "Trust Gap"
In space, sensors are liars. Standard GNSS signals jitter and drift by meters, providing a chaotic "uncertainty cloud" rather than a clean path. For a docking mission like **ISRO's SpaDeX**, trusting these raw "lies" would lead to a mission-ending collision.

### The Solution: A-ROD (Autonomous Relative Orbit Determination)
I architected A-ROD to act as a **mathematical gatekeeper**. It doesn't just "smooth" the noise; it arbitrates between what the sensors suggest and what the laws of physics allow.

---

## 🏗️ The Architecture
Instead of following data points blindly, the system enforces a **hierarchy of constraints**.

* **Physics-First Modeling**: I utilized **Clohessy-Wiltshire dynamics** to model relative motion in the **LVLH frame**. This ensures the chaser satellite adheres to unbreakable orbital invariants.
* **The Estimator**: I implemented an **Extended Kalman Filter (EKF)** using the **Joseph Form Covariance Update**. This specific architecture ensures numerical stability on flight-grade hardware.
* **Passive Safety**: The mission is designed around a **Safety Ellipse**. This is a fail-safe geometry: if the satellite loses all power, the natural physics of the orbit keep it circling safely rather than drifting into a crash.

---

## 📈 Performance & Results
By putting physics in tension with data, A-ROD achieves high-precision tracking even in "dirty" sensor environments.

| Metric | Raw Sensor Data | A-ROD (EKF) Result |
| :--- | :--- | :--- |
| **Position Jitter** | ±3–5 meters | **Sub-meter accuracy** |
| **Trajectory** | Stochastic/Jagged | **Smooth/Physics-Verified** |
| **Safety Risk** | High (Collision Course) | **Fail-Safe (Closed Loop)** |

---

## 🤖 The Architect’s Workflow
I served as the **System Architect** for this project, defining the mathematical framework and safety protocols. To bridge the gap between design and implementation, I used **AI as a "Co-Pilot"** to handle the boilerplate and syntax, allowing me to focus on high-level mission logic and numerical stability.

---

## 🚀 About the Developer
I am **Hani Mohammad Kaif**, a 6th-semester Electronics and Communication Engineering student at **St. Joseph Engineering College**. My focus is on bridging the gap between advanced signal processing and the future of autonomous space exploration.