# XRRpred-predictor
Implementation of XRRpred predictor: a predictor of X-ray structure quality from protein sequence
The source code provided here allows user to run XRRpred predictor on a local machine. 

**Note:** It is highly recommended that instead of using this repository, you use the docker implementation provided [here](https://github.com/sinaghadermarzi/XRRpred-docker), which is much easier. 
## Dependencies

#### 1-ASAquick and IUPred
XRRpred needs predictions of solvent accessibility from [ASAquick](http://mamiris.com/software.html) ([Faraggi et al. 2014](https://doi.org/10.1002/prot.24682)) and intrinsic disorder from [IUPred v1]() ([Dosztányi et al. 2017](https://onlinelibrary.wiley.com/doi/10.1002/pro.3334) and [Dosztányi et al. 2005](https://doi.org/10.1093/bioinformatics/bti541))  to make predictions. Therefore these programs should be installed on the system and their path should be entered in ``residuelevel_scores.py``. 
#### 2- python and python packages 
This code is developed and tested on python 3.8.3 but it should run on any version of python 3.
requirements packages are: sklearn, pandas and seaborn

## Prediction
to run, you just need to provide a fasta file (format as exmplained below) and run the following command in the root directory of the repository:

> ``python3 XRRpred.py seqs.fasta``

where `seqs.fasta` is the path to the fasta formatted input.

### Input format:
XRRPred accepts one or more proteins as input. The input protein sequences should be in the FASTA format, where for the multiple-chain proteins the chain sequences must use the same prefix in their ID (before the underscore). Example below shows the formatting for two proteins where proteinID1 has two chains (chainID1 and chainID2) and proteinID2 has one chain.

```
>proteinID1_chainID1
AMINOACIDSEQUENCE
>proteinID1_chainID2
AMINOACIDSEQUENCE
>proteinID2
AMINOACIDSEQUENCE
```

you can also look at the example file `example.fasta`

### Output
the output (the csv resutls and the visualizations) is stored in the same directory as the input file. You can find an example output in the `example` folder together with the corresponding input. 

