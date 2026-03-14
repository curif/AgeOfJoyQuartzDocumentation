This is a checklist to follow in order to create a correct `description.yaml` for your cabinet.

- [ ] Check the correct file name: is `description.yaml`
- [ ] Verify the [[YAML]] indentation. Read the [[CDL the Cabinet Description Language#YAML]] information.
- [ ] Search for misspelled yaml keys.
- [ ] Verify the required cabinet's parts and [[CDL the Cabinet Description Language#"Art" parts]] file names
- [ ] Add the [[md5 checksum]]  if your cabinet have a `rom`. You can get your md5 here: [MD5 Hash Calculator](https://curif.github.io/AgeOfJoy-ROMCRC/index.html)
- [ ] Verify the file name of the model (glb) it's ok, avoid a misspelled name.
- [ ] Set the `debug-mode: true` in the yaml file. Verify to not have errors in the [[CDL Debug mode#Debug information]] log file. Change it to false (or delete the line) upon distribution.
- [ ] Is a good practice to:
	- [ ] set the `author` key with your name information or [[Discord server]] user.
	- [ ] set the `comments` key with information about the cabinet
	- [ ] set the `year` of publication of the game
	- [ ] set the `version` (increment it to know that the cabinet was modified. Follow a [[semantic version system]])
- [ ] If your game have [[AGEBasic]] programs on it, check the [[AGEBasic programing#Debug mode]] and check for issues in the log files. Delete it upon distribution.
- [ ] Use [[ASTC textures]] when possible

#CDL 
