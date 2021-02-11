# XRRpred-predictor
Implementation of XRRpred predictor: a predictor of X-ray structure quality from protein sequence

The source code provided here allows user to run XRRpred predictor on a local machine. 
## Dependencies
This code is developed and tested on python 3.8.3 but it should run without problem on python 3.6 or any newer version.

### 1-ASAquick and IUPred
XRRpred needs predictions of solvent accessibility (from ASAquick) and intrinsic disorder (from IUPred v1) to make predictions. Therefore these programs should be installed on the system and their path should be entered in ``residuelevel_scores.py``. 
### 2- imported python packages
sklearn, numpy
## usage
to run, you just need to provide a fasta file fomatted the same way described on the XRRpred webserver (such as ``seqs.fasta``) and run the following command in the main directory:
> ./XRRpred.py seqs.fasta
