Operate the Basics
##################

Copy the wavgen package to the folder of your project, then try ``import wavgen`` or
``from wavgen import *``

.. important::
    The *package* is the nested directory, `wavgen/wavgen/`.

.. note::
    The package utilizes a number of *constants* & *parameters*, the latter which can be configured. The whole lot
    can be found in the :mod:`wavgen.config` module file.

Modules
=======
All of the functions relevant for user operation can be found in one of two user modules.

card.py
-------
Contains any & all code requiring Spectrum card drivers. Therefore, it is exclusively responsible for card
configuration & communication. (w/ 1 tiny :mod:`exception <wavgen.config>`)

Running
"""""""
Opening the card for use is simple::

    card = wv.Card()

You have the option to override the default output limit (in millivolts) or de/re-active the smoothing filter.
Then hand the card a :ref:`waveform object <wav>` and request operation::

    card.setup_channels(amplitude=240, use_filter=True)  # OPTIONAL

    card.load_waveforms(some_waveform_object)
    card.wiggle_output()

.. note::
    You could also pass a list of waveforms, ``card.load_waveforms([wav1, wav2, wav3])``, which will result
    in a concatenation of all waveforms, to be treated as a single monolithic waveform.

Stopping
""""""""
In the above example, a pop-up window offers a button to stop the card, which will otherwise run indefinitely.
To pre-determine an operation time, pass to the argument ``card.wiggle_output(duration=data)`` with a data of type:

float
    To set a fixed runtime in **milliseconds**
integer
    If you'd instead rather loop the waveform an integer number of **cycles**

Also through the use of a sequence :ref:`sequence <seq>`.

.. _wav:

waveform.py
-----------
Contains the data structures & associated routines for describing, calculating, and organizing parameterized
waveform templates.

.. warning::
    If you plan on running any waveform calculations, which will be except by explicitly loading from saved files, it
    is imperative that you enclose your script within::

        if __name__ == '__main__':
            ## Your Script ##

    to avoid issues with :ref:`parallelism <fix>`.

Bottom line, we need to give the card raw data-points for output. We achieve this by describing typical waveforms with
Python objects, containing parameters and an accompanying equation. You can either define a new waveform object, or use
on of the provided examples. All waveform objects are extensions of the :class:`wavgen.waveform.Waveform` class;
for example, the class definition heading for the **Superposition** waveform looks like
``class Superposition(Waveform):``..

Using Waveform
""""""""""""""
Here is an example script of how'd use the provided :class:`wavgen.waveform.Superposition` template; a waveform
encompassing an arbitrary combination of pure tone waves::

    from wavgen import *

    if __name__ == '__main__':
        card = wv.Card

        frequencies = [80E6 + j*1E6 for j in range(10)]  # Hertz
        initial_phases = np.arange(0, 2*pi, len(frequencies))
        A = wv.Superposition(frequencies, phases=initial_phases, milliseconds=10.0 *or* sample_length=int(16E3))
        A.compute_waveform()  # OPTIONAL, otherwise done at card start

        card.load_waveforms(A)

Saving
""""""

If a waveform calculation is lengthy, you can save the product to file for quicker reuse::

    A.compute_waveform("./saved_forms/wave_A")

.. _seq:

sequence
""""""""

card.load_sequence(segments, steps)
