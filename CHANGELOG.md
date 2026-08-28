# Changelog

## Unreleased

Plotting API cleaned up so figures can be embedded in a GUI (breaking):

- `Hyddb1.plot()` now returns the list of figures and no longer shows them;
  the `do_show` argument is gone. Call `matplotlib.pyplot.show()` yourself
  when running interactively.
- `Rao.plot`, `plot_amplitude`, `plot_phase` and `plot_surface` create their
  own figure when no `ax` is given instead of drawing into pyplot's "current
  axes" (which could be a figure owned by someone else), and return the Axes.
- Fixed: `Rao.plot_surface` with a single wave-direction drew a line plot and
  then an image on top of it; it now falls back to the line plot only.
- Fixed: `Rao.plot` labeled the y-axis "Amplitude" even when plotting phase,
  and always drew a legend even for a single direction.

## Version 2025.2.0

- Removed NetCDF4 in favour of hypy5, this solves fatal crashes that occured when reading a db twice.

## Version 2025.1.0

- Converted setup.cfg to pyproject.toml
- Fixed all unit tests

## Version 0.1

- Made creation methods static and renamed from `load` to `create`
