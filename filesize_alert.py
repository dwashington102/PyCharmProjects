"""
Script to monitor filesystems

File and directory names are stored in "monitored_items" text file.

Monitored directories:
/mnt/ibm_linux_mount/pmrs
/var/cache/yum

Files:
/var/log/message.*.log
/var/log/Xorg*.log
"""

# Import modules
import glob
import os
import re


"""
Header|Spacer|Footer
"""


def display_menu():
    os.system('clear')
    print("Gathering file sizes")


def add_spacer():
    print("========================================")


def get_messagelogs():
    with open('monitored_items', 'w') as mylist:
        for filelist in sorted(glob.glob('/var/log/message*')):
            mylist.write(filelist)
            mylist.write("\n")
    add_spacer()


def get_xorglogs():
    with open('monitored_items', 'a') as mylist:
        for filelist in sorted(glob.glob('/var/log/Xorg*')):
            mylist.write(filelist)
            mylist.write("\n")
    add_spacer()


def get_listfiles():
    with open("monitored_items", "r") as mylist:
        for my_filename in mylist:
                my_filename = re.sub(r'\n', '', my_filename)
                compute_fs_mb(my_filename)


def compute_fs_mb(my_filename):
    fsize_mb = float(os.path.getsize(my_filename)) / (1024 * 1024)
    print("Filename:", my_filename, "\t\t\tFilesize (MB): {:.2f}".format(fsize_mb))


# Call to action
display_menu()
get_messagelogs()
get_xorglogs()
get_listfiles()


# Out of here
print("End")
