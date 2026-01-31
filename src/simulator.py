import numpy as np
from typing import Tuple

class GNSSSimulator:
    """Professional Spacecraft Relative Dynamics Simulator."""
    def __init__(self, n_mean_motion: float):
        self.n = n_mean_motion 
        
    def _get_phi(self, t: float) -> np.ndarray:
        """Linearized State Transition Matrix (STM) for CW dynamics."""
        nt = self.n * t
        s, c = np.sin(nt), np.cos(nt)
        phi = np.zeros((6, 6))
        phi[0,0], phi[0,3], phi[0,4] = 4-3*c, (1/self.n)*s, (2/self.n)*(1-c)
        phi[1,0], phi[1,1], phi[1,3], phi[1,4] = 6*(s-nt), 1, (2/self.n)*(c-1), (1/self.n)*(4*s-3*nt)
        phi[2,2], phi[2,5] = c, (1/self.n)*s
        phi[3,0], phi[3,3], phi[3,4] = 3*self.n*s, c, 2*s
        phi[4,0], phi[4,3], phi[4,4] = 6*self.n*(c-1), -2*s, 4*c-3
        phi[5,2], phi[5,5] = -self.n*s, c
        return phi

    def generate_data(self, duration: float, dt: float, initial_state: np.ndarray, 
                      noise_pos: float = 3.0, noise_vel: float = 0.05) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        steps = int(duration / dt)
        t_vec = np.linspace(0, duration, steps)
        true_s, noisy_m = [], []
        
        for t in t_vec:
            phi_t = self._get_phi(t)
            state_t = phi_t @ initial_state
            true_s.append(state_t)
            noise = np.random.normal(0, [noise_pos]*3 + [noise_vel]*3)
            noisy_m.append(state_t + noise)
            
        return t_vec, np.array(true_s), np.array(noisy_m)