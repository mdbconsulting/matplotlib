from nose.tools import assert_raises
from mpl_toolkits.mplot3d import Axes3D, axes3d, proj3d
from matplotlib import cm
from matplotlib.testing.decorators import image_comparison, cleanup
from matplotlib.collections import LineCollection
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np


@image_comparison(baseline_images=['bar3d'], remove_text=True)
def test_bar3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
        xs = np.arange(20)
        ys = np.arange(20)
        cs = [c] * len(xs)
        cs[0] = 'c'
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)


@cleanup
def test_bar3d_dflt_smoke():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(4)
    y = np.arange(5)
    x2d, y2d = np.meshgrid(x, y)
    x2d, y2d = x2d.ravel(), y2d.ravel()
    z = x2d + y2d
    ax.bar3d(x2d, y2d, x2d * 0, 1, 1, z)
    fig.canvas.draw()


@image_comparison(baseline_images=['contour3d'], remove_text=True)
def test_contour3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-100, 100)


@image_comparison(baseline_images=['contourf3d'], remove_text=True)
def test_contourf3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-100, 100)


@image_comparison(baseline_images=['contourf3d_fill'], remove_text=True)
def test_contourf3d_fill():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(np.arange(-2, 2, 0.25), np.arange(-2, 2, 0.25))
    Z = X.clip(0, 0)
    # This produces holes in the z=0 surface that causes rendering errors if
    # the Poly3DCollection is not aware of path code information (issue #4784)
    Z[::5, ::5] = 0.1
    cset = ax.contourf(X, Y, Z, offset=0, levels=[-0.1, 0], cmap=cm.coolwarm)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-1, 1)


@image_comparison(baseline_images=['lines3d'], remove_text=True)
def test_lines3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z)


@image_comparison(baseline_images=['mixedsubplot'], remove_text=True)
def test_mixedsubplots():
    def f(t):
        s1 = np.cos(2*np.pi*t)
        e1 = np.exp(-t)
        return np.multiply(s1, e1)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    fig = plt.figure(figsize=plt.figaspect(2.))
    ax = fig.add_subplot(2, 1, 1)
    l = ax.plot(t1, f(t1), 'bo',
                t2, f(t2), 'k--', markerfacecolor='green')
    ax.grid(True)

    ax = fig.add_subplot(2, 1, 2, projection='3d')
    X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                           linewidth=0, antialiased=False)

    ax.set_zlim3d(-1, 1)


@image_comparison(baseline_images=['scatter3d'], remove_text=True)
def test_scatter3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np.arange(10), np.arange(10), np.arange(10),
               c='r', marker='o')
    ax.scatter(np.arange(10, 20), np.arange(10, 20), np.arange(10, 20),
               c='b', marker='^')


@image_comparison(baseline_images=['scatter3d_color'], remove_text=True,
                  extensions=['png'])
def test_scatter3d_color():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np.arange(10), np.arange(10), np.arange(10),
               color='r', marker='o')
    ax.scatter(np.arange(10, 20), np.arange(10, 20), np.arange(10, 20),
               color='b', marker='s')


@image_comparison(baseline_images=['surface3d'], remove_text=True)
def test_surface3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           lw=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    fig.colorbar(surf, shrink=0.5, aspect=5)


@image_comparison(baseline_images=['text3d'])
def test_text3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    zdirs = (None, 'x', 'y', 'z', (1, 1, 0), (1, 1, 1))
    xs = (2, 6, 4, 9, 7, 2)
    ys = (6, 4, 8, 7, 2, 2)
    zs = (4, 2, 5, 6, 1, 7)

    for zdir, x, y, z in zip(zdirs, xs, ys, zs):
        label = '(%d, %d, %d), dir=%s' % (x, y, z, zdir)
        ax.text(x, y, z, label, zdir)

    ax.text(1, 1, 1, "red", color='red')
    ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)
    ax.set_xlim3d(0, 10)
    ax.set_ylim3d(0, 10)
    ax.set_zlim3d(0, 10)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')


@image_comparison(baseline_images=['trisurf3d'], remove_text=True, tol=0.03)
def test_trisurf3d():
    n_angles = 36
    n_radii = 8
    radii = np.linspace(0.125, 1.0, n_radii)
    angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi/n_angles

    x = np.append(0, (radii*np.cos(angles)).flatten())
    y = np.append(0, (radii*np.sin(angles)).flatten())
    z = np.sin(-x*y)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)


@image_comparison(baseline_images=['wireframe3d'], remove_text=True)
def test_wireframe3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)


@image_comparison(baseline_images=['wireframe3dzerocstride'], remove_text=True,
                  extensions=['png'])
def test_wireframe3dzerocstride():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=0)


@image_comparison(baseline_images=['wireframe3dzerorstride'], remove_text=True,
                  extensions=['png'])
def test_wireframe3dzerorstride():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=0, cstride=10)

@cleanup
def test_wireframe3dzerostrideraises():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    with assert_raises(ValueError):
        ax.plot_wireframe(X, Y, Z, rstride=0, cstride=0)

@image_comparison(baseline_images=['quiver3d'], remove_text=True)
def test_quiver3d():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y, z = np.ogrid[-1:0.8:10j, -1:0.8:10j, -1:0.6:3j]

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))

    ax.quiver(x, y, z, u, v, w, length=0.1, pivot='tip', normalize=True)

@image_comparison(baseline_images=['quiver3d_empty'], remove_text=True)
def test_quiver3d_empty():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y, z = np.ogrid[-1:0.8:0j, -1:0.8:0j, -1:0.6:0j]

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))

    ax.quiver(x, y, z, u, v, w, length=0.1, pivot='tip', normalize=True)

@image_comparison(baseline_images=['quiver3d_masked'], remove_text=True)
def test_quiver3d_masked():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Using mgrid here instead of ogrid because masked_where doesn't
    # seem to like broadcasting very much...
    x, y, z = np.mgrid[-1:0.8:10j, -1:0.8:10j, -1:0.6:3j]

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))
    u = np.ma.masked_where((-0.4 < x) & (x < 0.1), u, copy=False)
    v = np.ma.masked_where((0.1 < y) & (y < 0.7), v, copy=False)

    ax.quiver(x, y, z, u, v, w, length=0.1, pivot='tip', normalize=True)

@image_comparison(baseline_images=['quiver3d_pivot_middle'], remove_text=True,
                  extensions=['png'])
def test_quiver3d_pivot_middle():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y, z = np.ogrid[-1:0.8:10j, -1:0.8:10j, -1:0.6:3j]

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))

    ax.quiver(x, y, z, u, v, w, length=0.1, pivot='middle', normalize=True)

@image_comparison(baseline_images=['quiver3d_pivot_tail'], remove_text=True,
                  extensions=['png'])
def test_quiver3d_pivot_tail():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y, z = np.ogrid[-1:0.8:10j, -1:0.8:10j, -1:0.6:3j]

    u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
    v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
            np.sin(np.pi * z))

    ax.quiver(x, y, z, u, v, w, length=0.1, pivot='tail', normalize=True)


@image_comparison(baseline_images=['axes3d_labelpad'], extensions=['png'])
def test_axes3d_labelpad():
    from nose.tools import assert_equal
    from matplotlib import rcParams

    fig = plt.figure()
    ax = Axes3D(fig)
    # labelpad respects rcParams
    assert_equal(ax.xaxis.labelpad, rcParams['axes.labelpad'])
    # labelpad can be set in set_label
    ax.set_xlabel('X LABEL', labelpad=10)
    assert_equal(ax.xaxis.labelpad, 10)
    ax.set_ylabel('Y LABEL')
    ax.set_zlabel('Z LABEL')
    # or manually
    ax.yaxis.labelpad = 20
    ax.zaxis.labelpad = -40

    # Tick labels also respect tick.pad (also from rcParams)
    for i, tick in enumerate(ax.yaxis.get_major_ticks()):
        tick.set_pad(tick.get_pad() - i * 5)


@image_comparison(baseline_images=['axes3d_cla'], extensions=['png'])
def test_axes3d_cla():
    # fixed in pull request 4553
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.set_axis_off()
    ax.cla()  # make sure the axis displayed is 3D (not 2D)

@cleanup
def test_plotsurface_1d_raises():
    x = np.linspace(0.5, 10, num=100)
    y = np.linspace(0.5, 10, num=100)
    X, Y = np.meshgrid(x, y)
    z = np.random.randn(100)

    fig = plt.figure(figsize=(14,6))
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    assert_raises(ValueError, ax.plot_surface, X, Y, z)


def _test_proj_make_M():
    # eye point
    E = np.array([1000, -1000, 2000])
    R = np.array([100, 100, 100])
    V = np.array([0, 0, 1])
    viewM = proj3d.view_transformation(E, R, V)
    perspM = proj3d.persp_transformation(100, -100)
    M = np.dot(perspM, viewM)
    return M


def test_proj_transform():
    M = _test_proj_make_M()

    xs = np.array([0, 1, 1, 0, 0, 0, 1, 1, 0, 0]) * 300.0
    ys = np.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 0]) * 300.0
    zs = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) * 300.0

    txs, tys, tzs = proj3d.proj_transform(xs, ys, zs, M)
    ixs, iys, izs = proj3d.inv_transform(txs, tys, tzs, M)

    np.testing.assert_almost_equal(ixs, xs)
    np.testing.assert_almost_equal(iys, ys)
    np.testing.assert_almost_equal(izs, zs)


def _test_proj_draw_axes(M, s=1, *args, **kwargs):
    xs = [0, s, 0, 0]
    ys = [0, 0, s, 0]
    zs = [0, 0, 0, s]
    txs, tys, tzs = proj3d.proj_transform(xs, ys, zs, M)
    o, ax, ay, az = zip(txs, tys)
    lines = [(o, ax), (o, ay), (o, az)]

    fig, ax = plt.subplots(*args, **kwargs)
    linec = LineCollection(lines)
    ax.add_collection(linec)
    for x, y, t in zip(txs, tys, ['o', 'x', 'y', 'z']):
        ax.text(x, y, t)

    return fig, ax


@image_comparison(baseline_images=['proj3d_axes_cube'], extensions=['png'],
                  remove_text=True, style='default')
def test_proj_axes_cube():
    M = _test_proj_make_M()

    ts = '0 1 2 3 0 4 5 6 7 4'.split()
    xs = np.array([0, 1, 1, 0, 0, 0, 1, 1, 0, 0]) * 300.0
    ys = np.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 0]) * 300.0
    zs = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) * 300.0

    txs, tys, tzs = proj3d.proj_transform(xs, ys, zs, M)

    fig, ax = _test_proj_draw_axes(M, s=400)

    ax.scatter(txs, tys, c=tzs)
    ax.plot(txs, tys, c='r')
    for x, y, t in zip(txs, tys, ts):
        ax.text(x, y, t)

    ax.set_xlim(-0.2, 0.2)
    ax.set_ylim(-0.2, 0.2)


def test_rot():
    V = [1, 0, 0, 1]
    rotated_V = proj3d.rot_x(V, np.pi / 6)
    np.testing.assert_allclose(rotated_V, [1, 0, 0, 1])

    V = [0, 1, 0, 1]
    rotated_V = proj3d.rot_x(V, np.pi / 6)
    np.testing.assert_allclose(rotated_V, [0, np.sqrt(3) / 2, 0.5, 1])


def test_world():
    xmin, xmax = 100, 120
    ymin, ymax = -100, 100
    zmin, zmax = 0.1, 0.2
    M = proj3d.world_transformation(xmin, xmax, ymin, ymax, zmin, zmax)
    np.testing.assert_allclose(M,
                               [[5e-2, 0, 0, -5],
                                [0, 5e-3, 0, 5e-1],
                                [0, 0, 1e1, -1],
                                [0, 0, 0, 1]])


@image_comparison(baseline_images=['proj3d_lines_dists'], extensions=['png'],
                  remove_text=True, style='default')
def test_lines_dists():
    fig, ax = plt.subplots(figsize=(4, 6), subplot_kw=dict(aspect='equal'))

    xs = (0, 30)
    ys = (20, 150)
    ax.plot(xs, ys)
    p0, p1 = zip(xs, ys)

    xs = (0, 0, 20, 30)
    ys = (100, 150, 30, 200)
    ax.scatter(xs, ys)

    dist = proj3d.line2d_seg_dist(p0, p1, (xs[0], ys[0]))
    dist = proj3d.line2d_seg_dist(p0, p1, np.array((xs, ys)))
    for x, y, d in zip(xs, ys, dist):
        c = Circle((x, y), d, fill=0)
        ax.add_patch(c)

    ax.set_xlim(-50, 150)
    ax.set_ylim(0, 300)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
