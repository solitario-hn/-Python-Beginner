#DEBUGGING
#1.AN ASSUMPTION TAKEN A LOOP MIGHT BE OUT OF RANGE


#REPROUDCING A bUG (jab koi kabhi kabhi hi aaraha ho kbhi kbhi nhi to hume dikkat aati h actual fault dhundhne me isliye hum ye method use krte hai )

from random import randint
dice_images=["1","2","3","4","5","6"]
dice_num=randint(0,5)
print(dice_num)
print(dice_images[dice_num])
#Shows index error as randint takes both uppe and lower limit values hence it gets out of range. and list has only index value 0-5

#so we produce bug and check out at which state it is causing an error one by one
#PLAY COMPUTER AND SEE WHEERE YOU'VE MISSED SOME STATEMENT OR MADE A MISTAKE THT COMPUTER IS NOT CONSIDERING THE COMMAND (WHICH U MIGHT'VE SKIPPED ACCIDENTALLY)
#searching up the error on the web yoou get during running the output
#try and except block except statemnts run when a value is occured tht you pass onto the except condition.
#using print statemnt to see what output is getting stored at each stage of the code.
#threads and variables show doff variables athe moment of what they're acc to the ste you're at the debugging process .
# step into (steps into the module) steps into my module (ignores python's own modules) step over(exeuctes the step till the breakpoint) , breakpoint.
#run after small steps to avoid bugs, ask it on stack overflow.(the last resort)
