> [!warning]
> This documentation has no utility, the information of this article remains for future development. Please do not follow this guide.



[[Age of Joy]] will use the folder path `/sdcard/Documents/AgeOfJoy` to storage all the information needed for the game simulation.

At start it will ask for permissions, please grant them.

If you decide to do not grant the permission, the alternative folder path is used: . 


> [!note]
> `/sdcard/Android/data/com.curif.AgeOfJoy` is deprecated but you could use it.
> 
> You could find references for both folders paths in the documentation.


## Older versions

If you are using an old version and you want to conserve the old folder access (`/sdcard/Android/data/com.curif.AgeOfJoy`) you don't need to do anything.

But if you want to change to the new one, follow these steps:

1. Quit [[Age of Joy]]
2. Rename the folder `/sdcard/Android/data/com.curif.AgeOfJoy/downloads` to another folder name. You can use [[Sidequest]] to do it.
3. Start [[Age of Joy]]. The process will detect that the `downloads` folder is missing (because you renamed it) and it will react like in a new installation.
4. Grant the permission (a window pops up). [[Age of Joy]] will create the new folder structure in `/sdcard/Documents/AgeOfJoy`. Read the Troubleshooting section below if the window not shown .
5. Quit [[Age of Joy]]
6. Move all the files and folders from `/sdcard/Android/data/com.curif.AgeOfJoy` to `/sdcard/Documents/AgeOfJoy

## Troubleshooting

It could be that the Quest stop asking for permissions at start of [[Age of Joy]]. Just quit, go to configuration -> App permissions -> Storage, search for the *Age of Joy* app and grant the permission manually. Repeat the process in [[AGEOfJoy storage permissions#Older version]] (above).

If you can't find AGE in the permission window, uninstall and reinstall it. Backup the folder `/sdcard/Android/data/com.curif.AgeOfJoy`` to your PC before the installation to do not loss anything


