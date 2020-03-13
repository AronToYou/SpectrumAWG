from lib import *

         #### IMPORTANT NOTES ####
# max value of amplitude: 2000mV. Do not exceed.
# For a given maximum amplitude of the card output, Vout,
# the amplitude of each pure tone will be (Vout / N) if
# N traps are output simultaneously.

# verboseprint = print if verbose else lambda *a, **k: None

## 20 Random Phases within [0, 2pi] ##
r = [2.094510589860613, 5.172224588379723, 2.713365750754814, 2.7268654021553975, 1.   /
     9455621726067513, 2.132845902763719, 5.775685169342227, 4.178303582622483, 1.971  /
     4912917733933, 1.218844007759545, 4.207174369712666, 2.6609861484752124, 3.41140  /
     54221128125, 1.0904071328591276, 1.0874359520279866, 1.538248528697041, 0.501676  /
     9726252504, 2.058427862897829, 6.234202186024447, 5.665480185178818]

# Define Waveform #
freq = [80E6 + j*1E6 for j in range(10)]
segmentA = Superposition(freqs=freq, waves=None, sample_length=16E3)
# segmentA.set_phases(r[:len(freq)])

# stable_A = SuperpositionFromFile('./waveforms/stable_A.h5py')
# stable_AB = SuperpositionFromFile('./waveforms/stable_AB.h5py')
# stable_B = SuperpositionFromFile('./waveforms/stable_B.h5py')
# stable_BA = SuperpositionFromFile('./waveforms/stable_BA.h5py')




# Open Card/Configure #
card = Card(mode='continuous')
card.setup_channels(amplitude=240)
card.load_sequence([segmentA])
# card.load_waveforms([stable_A, stable_AB, stable_B, stable_BA])
card.setup_buffer(verbose=True)

# A = Step(0, 0, 10000, 1)
# AB = Step(1, 1, 1, 2)
# B = Step(2, 2, 10000, 3)
# BA = Step(3, 3, 1, 0)
# card.load_sequence([A, AB, B, BA])

# Let it Rip #
card.wiggle_output(timeout=0, cam=False, verbose=True)

## Done! ##
print("Done -- Success!")


