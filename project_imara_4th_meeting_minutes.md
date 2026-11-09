# PROJECT IMARA — 4th Meeting Minutes

* **Date:** November 9, 2026
* **Time:** 17:33 UTC (8:33 PM EAT)
* **Attendees:** Rooney Ndereba (Team Lead), Michael Kimani, Winnie Wanjiku, Charles Njuguna, Dr. Elyas Smaida (Faculty Mentor)

---

## 1. Executive Summary

Project Imara simulations and hardware evaluations progressed significantly through component analysis, Python tool verification, and presentation planning:

* **Antenna Simulation and Tool:** Patch antenna simulations in Fairbeam/openEMS successfully reached $2.402\text{ GHz}$ ($S_{11} = -27.9\text{ dB}$) through physical length adjustments ($29.4\text{ mm} \to 27.5\text{ mm}$). The Python patch calculator tool computed necessary microstrip parameters and will be updated with supplier fabrication tolerances.
* **Hardware and Component Sourcing:** Hardware evaluations identified RF switches, LNAs, and connectors along with multi-receiver USB synchronization challenges. Budget allocations require revision to include international shipping, taxes, PCB fabrication, and test equipment/accessories to properly align with the $\text{US\$}1,500$ project funding scope.
* **Presentation and Submission Review:** Project submissions require a 5-page PDF documentation package by December 31, 2026. Dr. Elyas Smaida praised the logical structural flow of the team's presentations.

---

## 2. Key Decisions

* **Simulating the Antenna Concept:** The team aligned on focusing heavily on simulating the four-element dual-polarized antenna array concept and testing initial Wi-Fi sensing for the upcoming week before moving to the full Butler matrix layout.

---

## 3. Action Items & Next Steps

### Rooney Ndereba (Team Lead — Antenna & Simulation)
* [ ] **Design & Simulate Hardware:** Expand the single-patch simulation into the 4-element dual-polarized array, and coordinate simulations of the Butler matrix and phase-shifter array components to ensure the system meets functional requirements.
* [ ] **Send Meeting Minutes:** Distribute meeting minutes and outline specific next steps for the team.
* [ ] **Upload Files to GitHub:** Upload all project plans, role assignments, and simulation files discussed during the meeting to the GitHub repository in Markdown (`.md`) format.
* [ ] **Assign Weekly Duties:** Formally distribute simulation and research responsibilities among team members for the upcoming week.

### Michael Kimani (Software, Python & Sensing)
* [ ] **Update Calculator:** Incorporate substrate properties, simulated patch edge resistance, and supplier fabrication tolerances into `patch_calculator.py` to improve accuracy compared to current simulations.
* [ ] **Update Comparison Dashboard:** Update calculator inputs and compare the resulting theoretical figures against Fairbeam simulation data.
* [ ] **Build Interface & Array Model:** Develop the Python array-factor model and software display interface for system monitoring and Wi-Fi movement sensing.

### Winnie Wanjiku (Hardware Lead — Sourcing & Integration)
* [ ] **Collect Hardware Data (with Charles Njuguna):** Source exact substrate specifications, PCB stackup, and fabrication tolerances from online PCB manufacturers to finalize design specifications.
* [ ] **Research Amplifiers:** Investigate specific models of unidirectional low-noise amplifiers (LNAs) at $2.4\text{ GHz}$ to ensure signal quality and reverse isolation.
* [ ] **Verify Timing & Synchronization:** Analyze the timing accuracy requirements needed for simultaneous measurements across four ESP32 units and determine practical clock synchronization methods.
* [ ] **Refine Project Budget:** Revise the project budget (with Charles Njuguna) to properly reflect complete landed costs, PCB fabrication, shipping, taxes, and variations within the $\text{US\$}1,500$ target, justifying all component choices logically.

### Charles Njuguna (Hardware Support & Phase-Shifter Simulation)
* [ ] **Assist with Simulation:** Support the simulation effort by modeling the 4-channel phase-shifter array concept and assisting with the polarized array / Butler matrix evaluation.
* [ ] **Support Hardware & Budget Verification:** Work with Winnie Wanjiku to verify PCB fabrication tolerances and revise the comprehensive hardware budget.

### All Team Members
* [ ] **Ensure Receiver Compliance:** Verify that the hardware and firmware design strictly prevents any unintended transmission capabilities (receive-only compliance).
* [ ] **Format Project Documentation:** Edit all final documents and slides to remove formatting artifacts and normalize numerical styles for a clean, professional engineering presentation.

---

## 4. Detailed Discussion Notes

### 4.1 Project Imara & Antenna Simulation Progress (`00:00:47` – `00:14:39`)
* **Rooney Ndereba** introduced the Project Imara Dual-Mode ISAC system architecture utilizing commercial Wi-Fi routers, a reconfigurable polarized array with four dual-polarized patch antennas, a $4\times4$ Butler matrix for spatial sector division, and four ESP32 microcontrollers.
* Rooney reported using the Python calculator and parameters provided by **Michael Kimani** to simulate a single inset-fed patch antenna on $1.6\text{ mm}$ FR-4 in Fairbeam (`openEMS`).
* Initial simulations yielded an operating frequency of $2.316\text{ GHz}$ instead of the required $2.4\text{ GHz}$. After iteratively adjusting the patch length from $29.4\text{ mm}$ down to $27.5\text{ mm}$, Rooney successfully achieved a target resonant frequency of **$2.402\text{ GHz}$** with a return loss ($|S_{11}|$) of **$-27.9\text{ dB}$**, a bandwidth of $2.6\%$, and a directivity of $6.62\text{ dBi}$.

### 4.2 Development of the Python Patch Calculator Tool (`00:16:08` – `00:28:47`)
* **Michael Kimani** detailed the creation of a reusable Python tool (`patch_calculator.py`) designed to replace manual calculations by computing rectangular microstrip patch parameters and transmission-line values based on operating frequency and substrate properties.
* The tool incorporates formulas for patch width ($W$), effective permittivity ($\varepsilon_{\text{eff}}$ accounting for air and fringing effects on an FR-4 substrate), fringing length extensions ($\Delta L$), physical and electrical lengths, $50\text{ }\Omega$ and $35.35\text{ }\Omega$ line widths, $45^\circ$ and $90^\circ$ phase lengths, and inset notch width.
* The program includes input validation and geometry checks to flag invalid parameters.
* For next steps, Michael requested simulated patch edge resistance and tuned antenna geometry from Rooney, and supplier PCB stackup and fabrication tolerances from Winnie and Charles.

### 4.3 Hardware Component Selection & Cost Analysis (`00:31:00` – `00:45:26`)
* **Winnie Wanjiku** presented an evaluation of hardware components, comparing pSemi RF switches (`PE4259`) vs. Skyworks (`SKY13350`), ESP32 vs. STM32 microcontrollers, $50\text{ }\Omega$ SMA connectors, LNAs (`PSA4-5043+` vs. `TQP3M9037`), digital attenuators (`PE43711`), and the passive Butler matrix baseline vs. an active phase-shifter array.
* Winnie identified potential synchronization challenges when connecting four ESP32 receivers to a single USB hub due to internal clock drift, emphasizing the need to verify timestamp accuracy.
* Winnie also highlighted the strict contest rule requiring **receive-only operation**, noting that ESP32 firmware and hardware connections must be thoroughly verified to prevent accidental signal transmission.

### 4.4 Team Integration (`00:49:53`)
* **Charles Njuguna** reported on his integration into the team after joining the previous week, noting that his initial tasks involved catching up on project goals and assisting Winnie with the hardware evaluation. Charles committed to presenting independent work in the next meeting upon receiving his specific weekly assignment.

### 4.5 Project Submission Guidelines & Mentor Feedback (`00:51:42` – `00:59:38`)
* **Dr. Elyas Smaida** outlined the IEEE AP-S contest submission requirements, explaining that a **5-page PDF** documenting the ISAC system must be submitted by **December 31, 2026**. If selected among the top six finalist teams globally, the project will be funded and presented live in Tokyo, Japan.
* Evaluating the team's presentation structure, Dr. Smaida commended the logical flow from Rooney's high-level architecture and simulation overview to Michael's technical parameter breakdown and Winnie's hardware and financial analysis.
* Dr. Smaida advised the team to order future presentations by showing the full project simulation first, followed by the mathematical origins of specific parameters, and finally the hardware and costs.
* Dr. Smaida also advised the team to carefully proofread written documentation to remove any obvious AI formatting habits and normalize number formatting.

### 4.6 Budget Alignment & Scope (`01:01:53` – `01:12:05`)
* **Rooney Ndereba** and **Dr. Elyas Smaida** reviewed Winnie's initial local-currency component estimate and noted that it only covered bare individual chips without accounting for multi-board RF PCB fabrication, international courier shipping (DHL/FedEx from DigiKey/Mouser/JLCPCB), customs duties, coaxial assemblies, mechanical mounting, and backup spares.
* Dr. Smaida requested that Winnie and Charles revise the budget to realistically reflect the full landed project costs closer to the $\text{US\$}1,500$ budget ceiling while prioritizing sound engineering choices over merely filling the budget.

### 4.7 Schedule Review & Role Assignments (`01:03:54` – `01:13:48`)
* **Rooney Ndereba** noted that the team is currently ahead of schedule because electromagnetic simulation work has already begun in Week 3.
* Rooney outlined the next two weeks of work focusing on the 4-element dual-polarized patch array, phase-shifter modeling (assigned to Charles), Python array-factor and Wi-Fi sensing tests (assigned to Michael), and full BOM/receiver-chain analysis (assigned to Winnie).
* **Dr. Smaida** suggested using role-based or task-based labels rather than individual first names on formal presentation slides.
* **Michael Kimani** requested that all project documents be uploaded to the GitHub repository in readable format rather than shared only on WhatsApp, which Rooney agreed to do.

### 4.8 Live Fairbeam Simulation Walkthrough (`01:15:08` – `01:22:38`)
* At Michael's request, **Rooney Ndereba** shared his screen and conducted a live walkthrough of Fairbeam (`openEMS`), demonstrating how to open the inset-fed patch model, inspect the 12 design parameters (`patch_w = 38 mm`, `patch_l = 27.5 mm`, `inset = 9.8 mm`, `gap = 1 mm`, `feed_w = 3.06 mm`, `sub_h = 1.6 mm`, `eps_r = 4.4`), run the FDTD solver, and read the resulting $S_{11}$ return loss plot ($-27.9\text{ dB}$ at $2.402\text{ GHz}$).
* Following the demonstration, Michael confirmed he understood how the Python calculator outputs map directly into the Fairbeam simulation inputs.