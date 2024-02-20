"""The pint unit registry for pyElli"""

from pint import UnitRegistry

ureg = UnitRegistry()
ureg.enable_contexts("spectroscopy")

ureg.define("Angstroms = angstrom")
