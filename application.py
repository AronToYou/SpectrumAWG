from lib.spectrum_lib import *

         #### IMPORTANT NOTES ####
# max value of amplitude: 2000mV. Do not exceed.
# For a given maximum amplitude of the card output, Vout,
# the amplitude of each pure tone will be (Vout / N) if
# N traps are output simultaneously.

# Define Waveform
stable_A = SegmentFromFile('./waveforms/stable_A.h5py')

# Open Card/Configure #
card = OpenCard(mode='continuous')
card.setup_channels(amplitude=200)
card.load_segments([stable_A])  # , sweep_AB, stable_B, sweep_BA])
card.setup_buffer()

# Program Sequence #
step_A = Step(0, 0, 10000, 1)
step_AB = Step(1, 1, 1, 2)
step_B = Step(2, 2, 10000, 3)
step_BA = Step(3, 3, 1, 0)


# card.load_sequence([step_A, step_AB, step_B, step_BA])
# Let it Rip #

card.wiggle_output(timeout=0, cam=False, verbose=True)
"""
## Set all but one component's Magnitude to 0 ##
new_mags = np.zeros(len(segmentA.Waves), dtype=int)
new_mags[0] = 1
segmentA.set_magnitudes(new_mags)
segmentA.plot()
card.setup_buffer()

card.wiggle_output(timeout = 10000)
"""
## Done! ##
print("Done -- Success!")


