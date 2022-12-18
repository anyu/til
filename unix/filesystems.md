# Filesystems

(might have some Linux mixed in…)

Each file or directory is uniquely identified by its name, the directory in which it resides, and a unique identifier, typically called an inode.

| Directory      | Description |
| ----------- | ----------- |
| /      | root directory       |
| /bin   | where the executable files are located. These files are available to all users |
| /dev      | device drivers       |
| /etc      | supervisor directory commands, configuration files, disk configuration files, valid user lists, groups, ethernet, hosts, where to send critical messages.  Shouldn’t contain binaries       |
| /lib      | shared library files and sometimes other kernel-related files |
| /boot      | files for booting the system |
| /home      | home directory for users and other accounts |
| /mnt | used to mount other temporary file systems, such as cdrom and floppy for the CD-ROM drive and floppy diskette drive, respectively|
| /proc      |all processes marked as a file by process number or other information that is dynamic to the system |
| /tmp      | holds temporary files |
| /usr      | used for misc purposes, can be used by many users. (eg administrative commands, shared files, library files, etc) |
| /var      | typically contains variable-length files such as log and print files and any other type of file that may contain a variable amount of data |
| /sbin      | binary (executable) files, usually for system administration(eg fdisk and ifconfig utilities) |
| /kernel      | kernel files |


## Common Desktop Filesystem Types

| File Type      | Description |
| ----------- | ----------- |
| ext4      | This is the most current version of the native Linux filesystems. It is compatible with the older ext2 and ext3 versions. It supports disk volumes up to 1 exabyte and file sizes up to 16 terabytes and much more. It is the standard choice for Linux filesystems. |
| btrfs      | "Better or Butter FS" it is a new filesystem for Linux that comes with snapshots, incremental backups, performance increase and much more. It is widely available, but not quite stable and compatible yet. |
| XFS | High performance journaling file system, great for a system with large files such as a media server. |
| NTFS and FAT | Windows filesystems |
| HFS+ | mac filesystem |
