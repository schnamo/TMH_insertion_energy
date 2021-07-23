#!/bin/bash

# have pdb files for ref sequence
file_dir=$HOME"/TM_AF2/Predictions/"
file_dir_loop=$file_dir'*'

ref=$1
ref_dir=$HOME"/TM_AF2/ref_AF2/"
# where the reference sequences are stored
# tmalign_target=$ref_dir'ref_'$ref'.a3m.pdb'
tmalign_prefix=$HOME"/TM_AF2/tmalign_results/"
# where the resulting pw alignments are saved to, include ref seq name
tmalign_dir=$tmalign_prefix$ref'/'
# where the a3m files are stored
af2_dir=$HOME"/TM_AF2/Predictions/"

# ref1="O97467"
# ref2="P0AGF4"
# ref3="Q9LT15"

mkdir -p $tmalign_dir

for f in $file_dir_loop
 do

   # get sequence id
   fnew=${f##*/}
   fnew=${fnew%.*}
   # echo $fnew
   af2_in=$f
   tmalign_in=$af2_dir$fnew'.pdb'
   echo $tmalign_in

   tmalign_out=$tmalign_dir$fnew'_ali.txt'

   # use tmalign to align profile to reference profile
   ../TMalign $tmalign_in $ref_dir$ref'.a3m.pdb' >> $tmalign_out

 done
