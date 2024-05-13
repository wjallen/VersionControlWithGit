
Getting Set Up
==============

Prerequisites
-------------

1. `TACC account <https://accounts.tacc.utexas.edu/register>`_ (username, password, multifactor token)
2. `GitHub Account <https://github.com/signup>`_
3. `Docker Hub Account <https://hub.docker.com/signup>`_ (optional, but recommended)

Log in to Frontera
------------------

To log in to **Frontera**, follow the instructions for your operating system or
SSH client below.

.. attention::

   Replace ``username`` with your TACC username.

**Mac / Linux**

.. code-block:: console

   Open the application 'Terminal'
   type: ssh username@frontera.tacc.utexas.edu
   (enter password)
   (enter token)


**Windows**

* If using Windows Subsystem for Linux, refer to Linux instructions above
* If using an SSH client like PuTTY, refer to the steps below

.. code-block:: console

   Open your SSH client, e.g. 'PuTTY'
   enter Host Name: frontera.tacc.utexas.edu
   (click 'Open')
   (enter username)
   (enter password)
   (enter token)



Successful Login to Frontera
----------------------------

If your login was successful, your terminal will look something like this:

.. code-block:: console 

   Last login: Mon Apr 15 21:39:38 2024 from 129.114.64.2
   ------------------------------------------------------------------------------
                      Welcome to the Frontera Supercomputer
         Texas Advanced Computing Center, The University of Texas at Austin
   ------------------------------------------------------------------------------
   
                 ** Unauthorized use/access is prohibited. **
   
   If you log on to this computer system, you acknowledge your awareness
   of and concurrence with the UT Austin Acceptable Use Policy. The
   University will prosecute violators to the full extent of the law.
   
   TACC Usage Policies:
   http://www.tacc.utexas.edu/user-services/usage-policies/
   ______________________________________________________________________________
   
   Welcome to Frontera, *please* read these important system notes:
   
   --> Frontera user documentation is available at:
          https://portal.tacc.utexas.edu/user-guides/frontera
   
   ---------------------- Project balances for user wallen -----------------------
   | Name           Avail SUs     Expires | Name           Avail SUs     Expires |
   | TACC-SCI          101966  2025-06-30 | MCB22023             148  2024-06-30 | 
   | DesignSafe-DC       -418  2025-01-31 |                                      |
   ------------------------- Disk quotas for user wallen -------------------------
   | Disk         Usage (GB)     Limit    %Used   File Usage       Limit   %Used |
   | /home1              5.9      25.0    23.79        31772      400000    7.94 |
   | /work2            636.9    1024.0    62.20      2219251     3000000   73.98 |
   | /scratch1         512.5       0.0     0.00         3203           0    0.00 |
   | /scratch2        5997.0       0.0     0.00       597687           0    0.00 |
   | /scratch3           0.0       0.0     0.00            1           0    0.00 |
   -------------------------------------------------------------------------------
   
   Tip 143   (See "module help tacc_tips" for features or how to disable)
   
      Create a nifty overview of the hardware on your system and open the "hardware.html" in a browser:
          $ lshw -html > hardware.html




A Note About Quotas
-------------------

The welcome message you receive upon successful login to Frontera has useful information
for you to keep track of. Especially of note is the breakdown of disk quotas for your account,
as you can keep an eye on whether your usage is nearing the determined limit. 

Once your usage is nearing the quota, you will start to experience issues that will not only
impact your own work, but also impact the system for others. For example, if you're nearing
your quota in ``$WORK``, and your job is repeatedly trying (and failing) to write to ``$WORK``,
you will stress that file system.

Another useful way to monitor your disk quotas (and TACC project balances) at any time is to execute:

.. code-block:: console

   [fta]$ /usr/local/etc/taccinfo


