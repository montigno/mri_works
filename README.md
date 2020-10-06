[![](https://img.shields.io/badge/Python-3.5%2C%203.6%2C%203.7-yellow.svg)](#)
[![](https://img.shields.io/badge/platform-Linux-orange.svg)](#)
[![](https://img.shields.io/badge/license-CeCILL_b-blue.svg)](https://cecill.info/licences/Licence_CeCILL_V2.1-en.html)

mri_works is a graphical programming software written in Python and mainly intended for MRI image processing.\
It can be interfaced with many software and APIs : 
- Python : Numpy, Nilearn, Scipy, Matplotlib, Nipype (integrating FSL, Ants, SPM, AFNI)
- Java : ImageJ, MRIFileManager
- Matlab : SPM, MP3 ... and Matlab functions.
- Others : Dicomifier, MRTrix

Features :
- sequential or multiprocessing For Loop.
- 'If' structure.
- script tool.
- dynamic inputs.
- pipeline processing by [Capsul](http://brainvisa.info/capsul/index.html) or mri_works (integrating multithreading)
- possibility to create sub-modules
- bricks are very easy to make.

![title](https://montigno.github.io/mri_works/docs/Home/images/welcom01.png)

# Documentation

A beta documentation is available here : [https://montigno.github.io/mri_works](https://montigno.github.io/mri_works)

# Installation

See [here](https://montigno.github.io/mri_works/Home/install_mri_works.html)

# to launch the software

type *mri_works* in terminal

# License

mri_works is open source and is released under the [CeCILL-b software license](https://cecill.info/licences/Licence_CeCILL_V2.1-en.html).

# Release history

	21/08/2020 : Version 20.08.21a
	- MP3 modules integration
	- continued block documentation

<p></p>

	13/08/2020 : Version 20.08.13a
	- mri_works install into a virtual environment (venv)
	- compatibility with MATLAB engine
	- continued block documentation

<p></p>

	09/06/2020 : Version 20.06.09a
	- 'block documentation' windows replaced by tool tip
	- continued block documentation

<p></p>

	08/06/2020 : Version 20.06.08b
	- continued block documentation

<p></p>

	08/06/2020 : Version 20.06.08a
	- added 'legend' and 'block documentation' windows

<p></p>

	24/05/2020 : Version 20.05.24a
	- ScriptItem in LoopFor and If structure
	- block with dynamic enters now compatible with Capsul
	- add function 'join' for multiprocessing
	- blocks and examples added
	- some bugs fixed

<p></p>

    13/02/2020 : Version 20.02.00
	Features: 1st repository
