# waterCooledEngine

Initial scaffolding for steady-state FEM temperature analysis of a water-cooled rocket engine liner.

Purpose:
- Load geometry (CSV with `#` header comments, columns: x (mm), radius (mm)).
- Load simulation inputs from a YAML config file.
- Provide geometry parsing and a basic visualization to verify inputs.

Next steps: mesh generation and FEM solver integration (using SfePy / pygmsh / meshio).
