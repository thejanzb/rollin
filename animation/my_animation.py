#!/usr/bin/env python3
## Importing necessary packages
import numpy as np
import matplotlib.pyplot as plt
fname=''
# Dark Background Option
if(False): plt.style.use('dark_background'); fname='black_'
import matplotlib.animation as animation

big_rad = 0.5 ; small_rad = big_rad/2
fig = plt.figure(frameon=True, tight_layout=True)
# fig = plt.figure(frameon=False)
# fig = plt.figure()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
# x_margin = 0.1 ; y_margin = 0.1
# x_margin = 0 ; y_margin = 0
# ax = plt.axes(xlim=(-big_rad-x_margin, big_rad+x_margin), ylim=(-big_rad-y_margin, big_rad+y_margin))
# ax = plt.axes([0., 0., 1., 1.])
ax = plt.axes()
ax.set_aspect('equal')
line, = ax.plot([], [], lw=2)

def static_point_plot(th_P_0):
    x_vals = [big_rad*np.cos(th_P_0), big_rad*np.cos(th_P_0+np.pi)]
    y_vals = [big_rad*np.sin(th_P_0), big_rad*np.sin(th_P_0+np.pi)]
    ## Diameter Line Plot
    dia_P = plt.plot(x_vals, y_vals, color='blue')
    ## Point Plot
    dot_P, = plt.plot([x_vals[0]], [y_vals[0]], 'ro')
    return dia_P, dot_P

def animate_point_plot(dot_P, th_P_0, i):
    ## Point P animation
    rad_P = big_rad*np.cos(th_C_0 + omega*i - th_P_0)
    x_val = [rad_P*np.cos(th_P_0)]
    y_val = [rad_P*np.sin(th_P_0)]
    dot_P.set_data(x_val, y_val)
    return dot_P,
    
def init():
    line.set_data([], [])
    # x_val = small_rad*np.cos(th_C_0)
    # y_val = small_rad*np.sin(th_C_0)
    # small_circle= plt.Circle((x_val, y_val), radius=small_rad, color='b', fill=False)
    # ax.add_patch(small_circle)
    return line,# small_circle,

def animate(i):
    ## Points P, Q, R and S animation
    animate_point_plot(dot_P, th_P_0, i)
    animate_point_plot(dot_Q, th_Q_0, i)
    animate_point_plot(dot_R, th_R_0, i)
    animate_point_plot(dot_S, th_S_0, i)

    ## Small circle animation
    # New position for small circle center
    x_val = small_rad*np.cos(th_C_0 + omega*i)
    y_val = small_rad*np.sin(th_C_0 + omega*i)
    # Changing small circle center
    small_circle.center = (x_val, y_val)

    return dot_P, dot_Q, small_circle,

## Big Circle - Static in the background
big_circle = plt.Circle((0, 0), radius=big_rad, color='b', fill=False)
ax.add_patch(big_circle)

## omega of C (small circle centre) about O (big circle centre)
omega = np.pi/50

## Diameter including P - Static in the background
th_C_0 = np.pi/4

th_P_0 =   np.pi/4 ; dia_P, dot_P, = static_point_plot(th_P_0)
th_Q_0 = 2*np.pi/4 ; dia_Q, dot_Q, = static_point_plot(th_Q_0)
th_R_0 = 3*np.pi/4 ; dia_R, dot_R, = static_point_plot(th_R_0)
th_S_0 = 4*np.pi/4 ; dia_S, dot_S, = static_point_plot(th_S_0)

x_val = small_rad*np.cos(th_C_0)
y_val = small_rad*np.sin(th_C_0)
small_circle= plt.Circle((x_val, y_val), radius=small_rad, color='r', fill=False)
# plt.gca()
ax.add_patch(small_circle)

plt.axis('off')

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(round(2*np.pi/omega)), interval=10, blit=True)
## SAVE Routine
fname = fname + 'circ'
anim.save(fname+'.mp4', writer = 'ffmpeg', fps = 20, extra_args=['-vcodec', 'libx264'])
anim.save(fname+'.gif', fps = 20, writer = 'ffmpeg')
plt.show()