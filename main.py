import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from src.simulator import GNSSSimulator
from src.filter import RelativeEKF

# SEED DISABLED: The graph will now change every time you run it
# np.random.seed(42)

# --- CONFIG ---
N_LEO = 0.00113 
DT, DUR = 1.0, 5400 
INIT = np.array([50.0, 0.0, 10.0, 0.0, -0.113, 0.0])
GNSS_NOISE_STD = 3.0

# --- RUN ---
sim = GNSSSimulator(N_LEO)
t, true_s, noisy_m = sim.generate_data(DUR, DT, INIT, noise_pos=GNSS_NOISE_STD)
ekf = RelativeEKF(N_LEO, DT, r_val=GNSS_NOISE_STD**2)
ekf.x = noisy_m[0].reshape(-1, 1)

est = []
for i in range(len(t)):
    ekf.predict()
    est.append(ekf.update(noisy_m[i]))
est = np.array(est)

# --- VISUALIZATION ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(20, 10))
fig.suptitle("Relative Orbit Determination (ROD)\nGNSS Noise Suppression Engine Performance", fontsize=20, fontweight='bold')

ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(noisy_m[::5, 1], noisy_m[::5, 0], noisy_m[::5, 2], color='red', s=2, alpha=0.3, label='Raw Noisy GNSS')
ax1.plot(true_s[:, 1], true_s[:, 0], true_s[:, 2], color='cyan', linewidth=3, label='Ground Truth')
ax1.plot(est[:, 1], est[:, 0], est[:, 2], color='magenta', linestyle='--', linewidth=2, label='EKF Estimate')

# Full Axis Labels
ax1.set_xlabel("Along-Track (y) [m]", fontsize=12, labelpad=10)
ax1.set_ylabel("Radial (x) [m]", fontsize=12, labelpad=10)
ax1.set_zlabel("Cross-Track (z) [m]", fontsize=12, labelpad=10)

ax1.set_title("3D Relative Trajectory (LVLH Frame)", pad=20, fontsize=14)
ax1.legend(loc='upper right', facecolor='black')

ax2 = fig.add_subplot(122)
raw_err = np.linalg.norm(true_s[:, :3] - noisy_m[:, :3], axis=1)
ekf_err = np.linalg.norm(true_s[:, :3] - est[:, :3], axis=1)

ax2.fill_between(t, raw_err, color='red', alpha=0.4, label='Sensor Uncertainty Region')
ax2.plot(t, ekf_err, color='lime', linewidth=2, label='EKF Resultant Error')

ax2.set_xlabel("Mission Time [seconds]", fontsize=12)
ax2.set_ylabel("3D Absolute Position Error [meters]", fontsize=12)

ax2.set_title("Filter Convergence & Error Suppression", fontsize=14)
ax2.set_ylim(0, 10)
ax2.legend(loc='upper right')

plt.tight_layout(rect=[0, 0.03, 1, 0.92])
plt.savefig('SpaDeX_ROD_Stochastic_Final.png', dpi=300)
print("\n[COMPLETE] Stochastic report saved to: SpaDeX_ROD_Stochastic_Final.png")