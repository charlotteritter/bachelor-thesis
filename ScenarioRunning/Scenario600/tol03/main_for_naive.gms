$ONTEXT
Splitting into multiple files

True problem
ELiminnated X variables

$OFFTEXT

$eolcom //
OPTIONS PROFILE =3, RESLIM   = 2100, LIMROW   = 5, LP = CPLEX, MIP = cplex, RMIP=cplex, NLP = CONOPT, MINLP = DICOPT, MIQCP = CPLEX, SOLPRINT = OFF, decimals = 8, optcr=0.001, optca=0.001, threads =8, integer4=0;

********************************************************************************
$ include inputME.gms

** selbst eingefuegt, da sonst error 
$include subgradient_parameters.gms

** vorher: equation_true.gms
$include equations_all.gms   

********************************************************************************
*                                begin model
********************************************************************************


File NaiveSolve / NaiveSolve.csv /;
NaiveSolve.pc=5;
NaiveSolve.nd=5;
put NaiveSolve; 
put 'Gap Naive 1', put 'Gap Naive 2', put 'Gap Naive 3', put 'Gap Naive 4', put 'Obj. Naive', put 'Time Naive' put/;



set indices /1*6/;
Set TableSet /1*8/;

start_time = jnow;
solve schedule using MIP minimizing Obj ;
end_time = jnow ;

scalar ObjNaive;
ObjNaive=Obj.l;

scalar GapNaive1;
GapNaive1 = abs((schedule.objEst-schedule.objVal)/schedule.objEst);

scalar GapNaive2;
GapNaive2 = abs((schedule.objEst-schedule.objVal)/schedule.objVal);

scalar GapNaive3;
GapNaive3 = abs((schedule.objVal-schedule.objEst)/schedule.objVal);

scalar GapNaive4;
GapNaive4=abs(schedule.objVal-schedule.objEst)/max(abs(schedule.objVal),abs(schedule.objEst));  

run_time_total = ghour(end_time - start_time)*3600 + gminute(end_time - start_time)*60 + gsecond(end_time - start_time);

scalar TimeNaive;
TimeNaive=run_time_total;  

put NaiveSolve;
put GapNaive1, put GapNaive2, put GapNaive3, put GapNaive4, put ObjNaive, put TimeNaive put /;

display Obj.l, run_time_total ;



