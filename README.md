# TMH_insertion_energy
Inferring TMH insertion energies from reference sequences with known helix positions

## Data
| Folder/ File | Description | 
| ------------------------------------------------------ |------------------------------------------------------------------------------------------------------------------------|
| `reference_sequences` | Reference sequences and corresponding HHM-profiles |
| `sequences` | Sequences in fasta format |
| `profiles` | HHM-profiles created with hhblits against the UniRef30 database |
| `hhalign_X` | HMM-HMM alignment of every profile against reference profile X |
| `dgpred_results` | Inferred helices and corresponding dgpred energy calculations |
| `sequences.fasta` | All sequences in one fasta file |
| `TMH_insertion_energies.xlsx` | Energy values and sequences for 19 residue window and full length helices |

## Scripts

The python3 script `fasta_to_helices.py` takes as input a list of sequences in fasta format, corresponding HMM-profiles and HMM-HMM-alignments and infers the helices based on reference sequences with annotated structural information and calculates the corresponding energy values using dgpred.
