Graph Neural Networks and Transformer workshop
==============================================

.. raw:: html
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ZS00tnHVRbU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Graph Neural Networks and Transformers are neural network architectures which are quickly gaining in popularity due to how many problems can easily be modeled as graphs and sets. In this workshop we will take a deep dive into these architecture and how you can use them to solve complex problems where the input domain can be of different size.


.. prereq::

   This material assumes familiarity with deep learning, attendants should have implemented neural networks before using PyTorch. It also assumes basic understanding of linear algebra. Experience in working with graphs will make the material easier to go through, but is not considered a prerequsite.



The material is divided into four sessions, each corresponding to roughly 2 hours of work. The material is designed to be used on Google Colab, you can find links to the online notebooks in the offline versions maintained here.

.. toctree::
   :maxdepth: 1
   :caption: Presentations
   
   presentations


.. toctree::
   :maxdepth: 1
   :caption: Notebooks and colab

   notebooks_and_colab

   
.. toctree::
   :maxdepth: 1
   :caption: The Workshop

.. toctree::
   :maxdepth: 1
   :caption: Session 1

   notebooks/session_1/1a_representing_graphs_for_neural_networks_solutions.ipynb

.. toctree::
   :maxdepth: 1
   :caption: Session 1 extra material

   notebooks/session_1/1b_vector_sums_vs_concatenation.ipynb
   
.. toctree::
   :maxdepth: 1
   :caption: Session 2
   
   notebooks/session_2/2a_full_training_pipeline.ipynb

.. toctree::
   :maxdepth: 1
   :caption: Session 3
   
   notebooks/session_3/3a_Graph_Neural_Network_Encoder_solutions.ipynb

.. toctree::
   :maxdepth: 1
   :caption: Session 4
   
   notebooks/session_4/4a_GNNs_to_Transformers.ipynb
   

.. toctree::
   :maxdepth: 1
   :caption: Reference

   quick-reference
   guide


.. _learner-personas:

Who is the course for?
----------------------

This course is aimed at students, researchers, engineers and programmers who are already familiar with implementing neural networks in PyTorch and wants to understand the details about graph neural networks and transformers. The focus is on explaining the architectures and the choices involved in implementing a GNN, but does not look into detail of how to model diverse problems using the frameworks. The lessons assumes that the participant is familiar with:

- Programming in PyTorch - having implemented and trained a simple neural network
- Linear algebra - Basic understanding of linear transformations and vector arithmetics
- Machine learning - Basic understanding of training procedures and data issues



About the course
----------------

This lesson material is developed by the `EuroCC National Competence Center
Sweden (ENCCS) <https://enccs.se/>`_ and the `Research Institutes of Sweden <https://ri.se/>`_.

The lesson material is licensed under `CC-BY-SA-4.0
<https://creativecommons.org/licenses/by-sa/4.0/>`_ and can be reused in any form
(with appropriate credit) in other courses and workshops.
Instructors who wish to teach this lesson can refer to the :doc:`guide` for
practical advice.


Lesson format
-------------

The workshop material is based on Jupyter Notebooks designed for Google Colaboratory. 
You can find links to the noteboks under each lesson block. Before starting to work on the notebooks, 
you should create your own copy under `File->Save a copy in Drive`. This way changes you make to the 
notebook will remain, otherwise they will be lost when you close the colab window.


See also
--------
There are a growing number of resourses for graph neural network, here are good places to start:

* `Stanford CS224W: Machine Learning with Graphs <http://web.stanford.edu/class/cs224w/>`_. This material covers all manner of statistical learning on graphs, as well as many fundamental topics from graph theory. The lectures and notebook exercises from previous offerings of the course are available online.

* `Geometrical Deep Learning <https://geometricdeeplearning.com/>`_ : The Erlangen program of ML: This work by Bronstein et. al. takes a unifying perspective 
  on Graph Neural Networks and show how it encapsulates very general ideas in deep learning. There are multiple treatments, all of which are excellent:
  
  - `Invited talk <https://iclr.cc/virtual/2021/invited-talk/3717>`_ at ICLR 2021 lays out the ideas
  - The pre-print book `Geometric Deep Learning: Grids, Groups, Graphs, Geodesics and Gauges <https://arxiv.org/abs/2104.13478>`_ expands on this. 
  - A series of `video lecture <https://youtu.be/PtA0lg_e5nAwhich>`_ covers the material in depth.

* `PyTorch Geometric <https://pytorch-geometric.readthedocs.io/en/latest/>`_: This framework is quickly becoming the `de-facto` package for working with Graph Neural Networks. It doesn't support the Transformer approach we show in this workshop, but for regular Graph Neural Networks it's a high level framework with efficient kernels for sparse computation.





Credits
-------
The lesson file structure and browsing layout is inspired by and derived from
`work <https://github.com/coderefinery/sphinx-lesson>`_ by `CodeRefinery
<https://coderefinery.org/>`_ licensed under the `MIT license
<http://opensource.org/licenses/mit-license.html>`_. We have copied and adapted
most of their license text.
