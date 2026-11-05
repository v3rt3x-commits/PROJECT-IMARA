# PROJECT IMARA – PATCH ANTENNA CALCULATOR

## 1. Project Description

The Patch Antenna Calculator is a Python-based engineering tool developed for Project Imara. It performs preliminary calculations for a rectangular microstrip patch antenna and associated microstrip transmission lines operating at a specified frequency.

## 2. Features

The calculator determines:

- Patch width and physical length.
- Effective dielectric constant.
- Fringing length extension.
- Inset feed depth.
- 50-ohm feed-line width.
- 35.35-ohm transmission-line width.
- Quarter-wavelength transmission-line lengths.
- 45-degree and 90-degree electrical phase lengths.
- Inset notch width.

It also performs basic input and geometry validation.

## 3. Requirements

- Python 3
- Python `math` module (included in Python)

No additional libraries are required.

## 4. How to Run

Open a terminal in the project folder and execute:

`python patch_calculator.py`

Follow the prompts and enter the requested antenna parameters.

## 5. Required Inputs

| Input | Description |
|---|---|
| Operating frequency | Antenna operating frequency in GHz |
| Patch edge resistance | Resistance obtained from antenna simulation, in ohms |
| Dielectric constant | Relative permittivity of the substrate |
| Substrate thickness | Thickness of the dielectric substrate, in mm |
| Notch clearance | Clearance on each side of the feed line, in mm |

## 6. Engineering Considerations

The calculator provides preliminary theoretical dimensions. Its results must be checked using electromagnetic simulation before PCB fabrication.

Actual substrate specifications, simulated patch edge resistance, fabrication tolerances and the selected Butler Matrix topology must be confirmed before finalising the design.

## 7. Project

Project Imara – ISAC Antenna and Sensing System.

**Development:** Michael Kimani
