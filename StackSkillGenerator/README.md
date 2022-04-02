# Stack Skill Generator
Script to handle a bulk of the work when creating a custom skill for an item with a custom stack count, the ouput can be pasted into blcmm just make sure to put the comment lines in seperately.
The code will require command extentiosn to work.

When running the code make sure to have blueprint.txt in the same folder as the script.
Run the script as "skillgen.py BASEOBJ TRUEMAXSTACKS FAKEMAXSTACKS SKILLEVENT SKILLDURATION SKILLHUDSLOT TRACKEDICON" adding your own info for the command line args which are the following:
 - BASEOBJ: The name of the object this will all apply to.
 - TRUEMAXSTACKS: The actual effective max stacks of the bonus that will apply.
 - FAKEMAXSTACKS: The max stacks of the actually stacking skill, making this greater than TRUEMAXSTACKS allows for a buffer before the effect starts to decay.
 - SKILLEVENT: The name of the event that will cause the skill to stack.
 - SKILLDURATION: How long each stack will last.
 - SKILLHUDSLOT: The hud slot of the skill.
 - TRACKEDICON: The icon of the skill (what will show in the tracked slot).
