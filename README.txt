Where to find the results:

The results tables are stored in "Results" --> "Final Results". 
- The folder "Scenarios" is filled with the results for the regular scenario files (from section 3.2)
- "Samples" is filled with the compiled results for the different big random scenario samples we used for the statistical tests in 3.3 and 3.4. 
  The subfolders "100Scen", "600Scen", "900Scen" give information about the amount of scenarios in the samples, whose results are stored in the folders.
01, 03, 05 and 07 in the xlsx files tells us the tolerance epsilon (0.01,0.03,0.05,0.07) which was used to get the results in the file.

------------------------------------------------------------------------------------------------------------------------------------------------------

How to run the program, which calculates solutions for the Naive approach and the LR with all six different step size rules:

1. Navigate to the folder with the inputs you want to run the program with: 
   --> "SampleRun_Environment" is the folder for running the program with the random scenario samples from secion 3.3. and 3.4. 
       Select the size of the scenario sample by choosing "100Scens", "600Scens" or "900Scens". Then choose the value of the tolerance epsilon (0.01,0.03,0.05,0.07).
       The subfolders "Scenario1" to "Scenario20" tell us which sample we used, because in total we had 20 random samples. 
       In those folders there are all input files and .gms files included, which we need for running the program.
   --> "ScenarioRunning" includes the input data for the regular scenario files we used in section 3.2. First choose the size of the Scenario set (150,300,450
       600,900,1200), then the tolerance epsilon (0.01,0.03,0.05,0.07). In that folder all inputs we need for running the program are included.
2. Run the program by running "Naive_LR_solving.gms" with gams
3. Wait for it to finish (depending on the size of the scenario sample and tolerance epsilon, it can take quite some time, max. 9h)
4. Read the results from "TestingFile.csv" file, which is created by the program.


Possible problems:

It seldom occured that there was some computational error in the calculations, because the solution of the LR was smaller than the Naive solution
and accordingly the gap of the LR then negative, which shouldn't be the case. Whenever that occurs, we solved the step size for which the error occured individually 
with the "main_for_lr.gms". Therefore we just need to change the step rule in the gams file to the one we need and then run the "main_for_lr.gms" file with gams. 
Then we can read the LR solution (called lowerbound in the program) and attributes from the created "main_for_lr.lst" file.

In "RandomSampleScenarioInputFiles" you can find all the randomly generated scenario files for the statistic tests of section 3.3 and 3.4, also in a sorted
file for the lower bound heuristic we described in section 2.2.3 of the bachelor thesis. 