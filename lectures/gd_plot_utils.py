import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

squared_loss_fun = lambda pred, y: np.sum((pred-y[:,None])**2,axis=0)

# reading/understanding this plotting code is optional
def plot_loss(loss_fun, X, y, steps = []): 
    m = 70
    w_lin = np.linspace(-500.0, 500.0, m)
    b_lin = np.linspace(-500.0, 500.0, m)
    w_grid, b_grid = np.meshgrid(w_lin, b_lin)
    w_flat = w_grid.flatten()
    b_flat = b_grid.flatten()
    
    pred = w_flat[None]*X + b_flat[None]

    loss = loss_fun(pred, y) 
    loss_grid = np.reshape(loss,[m,m])

    fig, ax = plt.subplots()
    im = plt.imshow(loss_grid, interpolation='bilinear', origin='lower',
                cmap=cm.Wistia, extent = (-500, 500, -500, 500))
    CS = ax.contour(w_grid, b_grid, loss_grid, 20)
    imin = np.argmin(loss_grid)
    ax.plot(w_flat[imin], b_flat[imin], 'r*', markersize=15)
    plt.xlabel('$w$')
    plt.ylabel('$w_0$')
    #plt.clabel(CS, inline=1, fontsize=10)
    plt.title('Loss in $w$-$w_0$ space')
    ax.set_aspect("equal")
    plt.show()
              

def make_plot_pairs(w,β,t,Nsteps,x,y,titles=False,figheight=50): 
    X = x[:,None] 

    plt.subplot(Nsteps+1,2,2*t+1)    
    plt.plot(x,y,'.')
    plt.plot(x,w[-1]*x+β[-1])
    plt.ylabel('iteration %d' % t)
    if titles:
        plt.title("Data space: Epoch %d"%t)
    
    plt.subplot(Nsteps+1,2,2*t+2)
    fig = plt.gcf()
    fig.set_figheight(figheight)
    m = 70
    w_lin = np.linspace(-500.0, 500.0, m)
    β_lin = np.linspace(-500.0, 500.0, m)
    w_grid, β_grid = np.meshgrid(w_lin, β_lin)
    w_flat = w_grid.flatten()
    β_flat = β_grid.flatten()
    pred = w_flat[None]*X + β_flat[None]
    loss = squared_loss_fun(pred, y) 
    loss_grid = np.reshape(loss,[m,m])
    imin = np.argmin(loss_grid)
    plt.plot(w_flat[imin], β_flat[imin], 'r*', markersize=10)
    im = plt.imshow(loss_grid, interpolation='bilinear', origin='lower',
                cmap=cm.Wistia, extent = (-500, 500, -500, 500))
    CS = plt.contour(w_grid, β_grid, loss_grid,15)
    plt.plot(w, β, 'b-*', markersize=6)
    #plt.clabel(CS, inline=1, fontsize=10)
    if titles:
        plt.title("Parameter space: Epoch %d"%t)



def make_alpha_plots(alpha_vals, X, y):
    # functions to compute the loss and gradient
    f = lambda w: np.sum((X@w-y)**2)/2
    df= lambda w: X.T@(X@w) - X.T@y

    d = X.shape[1]

    plt.figure(figsize=(8,8))
    plt.subplot(2,1,1)
    loss = dict()
    for alpha in alpha_vals:
        w = np.zeros((d,1)) # initialize parameters
        grad_f = df(w)
        loss[alpha] = [f(w)]
        while np.linalg.norm(grad_f) > 0.001:
            grad_f = X.T@(X@w) - X.T@y
            w -= alpha*grad_f
            loss[alpha].append(f(w))
            if loss[alpha][-1] > loss[alpha][0]:
                break

        plt.plot(loss[alpha], label="alpha = %s"%alpha)
    plt.legend();
    plt.xlabel("iterations");
    plt.ylabel("loss");
    plt.title("Loss vs. iterations for different learning rates");
    
    plt.subplot(2,1,2)
    plt.plot(alpha_vals, [len(loss[alpha]) if loss[alpha][-1]<loss[alpha][0] else 1000 for alpha in alpha_vals]);
    plt.xlabel("alpha");
    plt.ylabel("iterations");
    plt.title("Iterations until convergence");
    
    plt.tight_layout()
