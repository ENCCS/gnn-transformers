Running the material on the LUMI super computer
===============================================

In this guide we will go through how you can run the workshop material on the LUMI super computer.

Prerequesits
------------

You will need a user account at LUMI and be able to connect through SSH to the login nodes. This will also have left you with a pair of SSH keys, you will need them later in this guide.

Copying the workshop material
-----------------------------

Once you are logged in at a login node, you need to copy the workshop material to your home directory. To handle changes in the notebooks, we use git to track changes.

.. code-block:: shell

   YOUR_USERNAME@uan01:~> git clone /project/project_465000485/gnn_transformers_workshop/gnn_transformers_notebooks $HOME/notebooks

This creates a new directory called ``notebooks`` in your home directory. This is a git repository which refers to a directory in the project folder. You can update this directory to the latest version using:

.. code-block:: shell

   YOUR_USERNAME@uan01:~> git -C $HOME/notebooks pull



Starting a jupyter notebook server
----------------------------------

Once the material is copied to your home directory you can start the jupyter server as a batch job:

.. code-block:: shell

   YOUR_USERNAME@uan01:~> /project/project_465000485/gnn_transformers_workshop/start-jupyter.sh

This will do a couple of things:

 - First it will submit a batch script (located in ``/project/project_465000485/gnn_transformers_workshop/start-jupyter.sh``) to 
   the Slurm resource management system.This script sets up a jupyter notebook server as 
   well as a SSH server on the compute node. The server assumes that there's a ``$HOME/notebooks`` directory, if not it will fail to start. Please perform the step above "Copying the workshop material".
 - It then starts monitoring the output file from of the slurm job (named something like slurm_JOBID.out) 
   using the `tail` program.

Eventually, once the jupyter server has started you will get some output like the one below. The important sections are highlighted:

.. code-block:: shell
    :emphasize-lines: 5,10,11,18

    Run on local machine to forward jupyter from Lumi

    Linux / macOS / MobaXTerm / Cmder:
    -----------------------------------------------------------------
    ssh -N -L 8888:nid005517-nmn:8888  YOUR_USERNAME@lumi.csc.fi
    -----------------------------------------------------------------

    PuTTy:
    -----------------------------------------------------------------
    ssh -N -L 8888:nid005517-nmn:8888 YOUR_USERNAME@lumi.csc.fi
    Set Source (8888) and Destination (nid005517-nmn:8888) in:
    PuTTy -> Connection -> SSH -> Tunnels
    -----------------------------------------------------------------


    Copy/Paste this URL into your browser
    -----------------------------------------------------------------
    http://localhost:8888/?token=36ffa17d87a728f3e4611234e6957afafc35e6ae30f63d82
    -----------------------------------------------------------------

These are the instructions you need to follow to connect to the compute node, in this 
example the compute node has the hostname ``nid005517-nmn``, but you will in all 
likelihood have a different one. What you see displayed is the output of your slurm job, 
you can safely exit from this display using ``CTR-C``. The script also exports the ID of the job to the environmental variable ``$JOB_ID``, so you can easily cancel the job by just running:

.. code-block:: shell
    # You can run this command if you wish to cancel the job 
    you@your_own_machine:~> scancel $JOB_ID


Note that you need to also tell ssh what key to use, 
so if for example your key is located in `~/.ssh/lumi_ed25519`, use the command:

.. code-block:: shell

    you@your_own_machine:~> ssh -N -L 8888:nid005517-nmn:8888  YOUR_USERNAME@lumi.csc.fi -i ~/.ssh/lumi_ed25519


Once you have run this command you now have a tunnel connecting the port 8888 at your local machine to port 8888 (which the jupyter server is listening to) at the compute node.

**N.B. This SSH connection need to be open during the time you use jupyter, it acts as a tunnel between your local computer and the jupyter server on the compute node.**

If you get an error message that the port is unavailable you are likely running jupyter locally. In this case, forward another local port (e.g. 8900) to the compute node:

.. code-block:: shell

    # Only run this if your local port 8888 is unavailable
    you@your_own_machine:~> ssh -N -L 8900:nid005517-nmn:8888  YOUR_USERNAME@lumi.csc.fi -i ~/.ssh/lumi_ed25519


Now you can open a browser pointing it to the local host, using the URL highlighted in the output. You should be greeted by a jupyter server directory listing.

.. Optional: Adding entries to the SSH config file
.. -----------------------------------------------

.. Since you will connect multiple times to the cluster, adding some entries to your SSH config file can be convienient. If you want  to do this, add the following to the config file on your local computer (by default in ``~/.ssh/config``):

.. .. code-block:: ssh-config

..     Host lumi
..         HostName lumi.csc.fi
..         Port 22
..         User YOUR_USERNAME  # Replace this with your username
..         IdentityFile ~/.ssh/lumi_ed25519  # Replace this with the path to your LUMI private key

..     Host nid005517-nmn
..         Port 22
..         User YOUR_USERNAME
..         IdentityFile ~/.ssh/id_ed25519_mlux
..         ProxyJump lumi
..         RequestTTY yes
..         LocalForward 8888 localhost:8888