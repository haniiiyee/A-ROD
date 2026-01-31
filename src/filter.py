import numpy as np

class RelativeEKF:
    """ISRO-Standard Extended Kalman Filter with Joseph Form Stability."""
    def __init__(self, n: float, dt: float, q_val: float = 0.001, r_val: float = 9.0):
        self.n, self.dt = n, dt
        self.x = np.zeros((6, 1))      
        self.P = np.eye(6) * 100.0     
        self.Q = np.eye(6) * q_val     
        self.R = np.eye(6) * r_val     
        self.H = np.eye(6)             

    def predict(self):
        nt = self.n * self.dt
        s, c = np.sin(nt), np.cos(nt)
        Phi = np.zeros((6, 6))
        Phi[0,0], Phi[0,3], Phi[0,4] = 4-3*c, (1/self.n)*s, (2/self.n)*(1-c)
        Phi[1,0], Phi[1,1], Phi[1,3], Phi[1,4] = 6*(s-nt), 1, (2/self.n)*(c-1), (1/self.n)*(4*s-3*nt)
        Phi[2,2], Phi[2,5] = c, (1/self.n)*s
        Phi[3,0], Phi[3,3], Phi[3,4] = 3*self.n*s, c, 2*s
        Phi[4,0], Phi[4,3], Phi[4,4] = 6*self.n*(c-1), -2*s, 4*c-3
        Phi[5,2], Phi[5,5] = -self.n*s, c
        self.x = Phi @ self.x
        self.P = Phi @ self.P @ Phi.T + self.Q

    def update(self, z: np.ndarray) -> np.ndarray:
        z = z.reshape(-1, 1)
        y = z - (self.H @ self.x) 
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S) 
        self.x = self.x + K @ y
        I = np.eye(6)
        IKH = I - K @ self.H
        self.P = IKH @ self.P @ IKH.T + K @ self.R @ K.T
        return self.x.flatten()