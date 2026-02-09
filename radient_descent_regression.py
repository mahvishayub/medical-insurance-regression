import numpy as np

def hypothesis(Xb, theta):
    return Xb @ theta

def compute_cost(Xb, y, theta, lam=10):
    m = len(y)
    error = Xb @ theta - y
    cost = (1 / (2 * m)) * np.sum(error ** 2)
    cost += (lam / (2 * m)) * np.sum(theta[1:] ** 2)
    return cost

def gradient(Xb, y, theta, lam=10):
    m = len(y)
    error = Xb @ theta - y
    grad = (1 / m) * (Xb.T @ error)
    grad[1:] += (lam / m) * theta[1:]
    return grad

def gradient_descent(Xb, y, alpha=0.01, iters=5000, lam=10):
    theta = np.zeros((Xb.shape[1], 1))
    J_history = []
    for _ in range(iters):
        grad = gradient(Xb, y, theta, lam)
        theta -= alpha * grad
        J_history.append(compute_cost(Xb, y, theta, lam))
    return theta, J_history
